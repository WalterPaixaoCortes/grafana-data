# -*- coding: utf-8 -*-

import csv
import os
import datetime
import re
import traceback

import typer

from sqlalchemy import func, and_, desc, asc

from pcf_logging import pcf_logger
import database as db
import config
from models import SurveyData

db.init()


def load_data(name: str, clean: bool = False):
    raw_data = []

    dbcon = db.get_db()

    id = dbcon.query(func.Max(SurveyData.id)).scalar()

    if id is None:
        id = 1
    else:
        id += 1

    pcf_logger.info('Processing file {0}'.format(name))
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        csvR = csv.DictReader(fr)
        mbr = 1
        metadata = (name.replace('.csv', '')).split('_')
        regex = r"^(.*)\_[0-9]$"
        for item in csvR:
            for idx, key in enumerate(item.keys()):
                match = re.search(regex, key, re.MULTILINE)
                category = None

                if match:
                    question = match.group(1)
                    category = 'None'
                else:
                    question = key

                record = {
                    'id': id,
                    'respondent': 'Respondent_%s' % mbr,
                    'question': question,
                    'category': category,
                    'answer': (item[key].encode('utf-8', errors='replace')).decode('utf-8'),
                    'load_date': datetime.datetime.now(),
                    'application': metadata[0],
                    'survey_name': metadata[1]
                }

                raw_data.append(record)
                id += 1
            mbr += 1

    pcf_logger.info("Number of loaded records: {0}" .format(len(raw_data)))

    if clean:
        pcf_logger.info('Cleaning old survey data...')
        dbcon.query(SurveyData).filter(and_(SurveyData.application ==
                                            metadata[0], SurveyData.survey_name == metadata[1])).delete()
        dbcon.commit()

    offset = dbcon.query(func.Count(SurveyData.id)).filter(
        SurveyData.application == metadata[0]).scalar()

    pcf_logger.info('Saving into database...')
    pcf_logger.info("Offset records: {0}" .format(offset))
    comm_lim = 1
    try:
        for idx, item in enumerate(raw_data):
            if idx > offset:
                elem = SurveyData(**item)
                dbcon.add(elem)
                comm_lim += 1
                if comm_lim % 15 == 0:
                    dbcon.commit()
                    pcf_logger.info('{0} records saved.'.format(comm_lim))
        dbcon.commit()
    except:
        pcf_logger.info(traceback.format_exc())


if __name__ == "__main__":
    typer.run(load_data)
