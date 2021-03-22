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
from models import NetflixViewHistory

db.init()


def load_data(name: str, clean: str):
    raw_data = []
    dbcon = db.get_db()

    id = dbcon.query(func.Max(NetflixViewHistory.id)).scalar()
    if id is None:
        id = 1
    else:
        id += 1

    pcf_logger.info('Processing file {0}'.format(name))
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        csvR = csv.DictReader(fr)
        metadata = (name.replace('.csv', '')).split('_')
        regex = r"^(.*):(.*):(.*)$"
        for item in csvR:
            record = {
                'id': id,
                'conta': metadata[0],
                'perfil': metadata[1],
            }

            match = re.search(regex, item['Title'], re.MULTILINE)

            if match:
                record['tipo'] = 'Série'
                record['titulo'] = match.group(1)
                record['temporada'] = match.group(2)
                record['episodio'] = match.group(3)
            else:
                record['tipo'] = 'Filme'
                record['titulo'] = item['Title']
                record['temporada'] = None
                record['episodio'] = None

            raw_data.append(record)
            id += 1

    pcf_logger.info('Saving into database...')

    if clean.upper() == 'SIM':
        dbcon.query(NetflixViewHistory).filter(and_(NetflixViewHistory.conta ==
                                                    metadata[0], NetflixViewHistory.perfil == metadata[1])).delete()

    i = 1
    for item in raw_data:
        try:
            elem = NetflixViewHistory(**item)
            dbcon.add(elem)
            i += 1
            if i % 10 == 0:
                dbcon.commit()
                pcf_logger.info('Saved {0} records.'.format(i))
        except:
            pcf_logger.info(item)

    dbcon.commit()


if __name__ == "__main__":
    typer.run(load_data)
