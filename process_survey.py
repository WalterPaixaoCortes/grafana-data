# -*- coding: utf-8 -*-

import csv
import os
import datetime
import re

import typer

from sqlalchemy import func, and_, desc, asc

from pcf_logging import pcf_logger
import database as db
import config
from models import SurveyData

db.init()


def load_data(name: str):
    raw_data = []

    pcf_logger.info("Getting last id")
    dbcon = db.get_db()

    id = dbcon.query(func.Max(SurveyData.id)).scalar()
    if id is None:
        id = 1
    else:
        id += 1

    pcf_logger.info('Next id = {0}'.format(id))

    pcf_logger.info('Processing file {0}'.format(name))
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        csvR = csv.DictReader(fr)
        mbr = 1
        metadata = (name.replace('.csv', '')).split('_')
        regex = r"^.*\[(.*)\]$"
        for item in csvR:
            for idx, key in enumerate(item.keys()):
                match = re.search(regex, key, re.MULTILINE)
                category = None

                if match:
                    question = key.replace('['+match.group(1)+']', '')
                    category = match.group(1)
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

    pcf_logger.info('Saving into database...')

    dbcon.query(SurveyData).filter(and_(SurveyData.application ==
                                        metadata[0], SurveyData.survey_name == metadata[1])).delete()

    for item in raw_data:
        try:
            elem = SurveyData(**item)
            dbcon.add(elem)
        except:
            pcf_logger.info(item)
    dbcon.commit()


if __name__ == "__main__":
    typer.run(load_data)
