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
    dbcon = db.get_db()

    id = dbcon.query(func.Max(NetflixViewHistory.id)).scalar()
    if id is None:
        id = 1
    else:
        id += 1

    for file in os.listdir(os.path.join(config.GRAFANA_DATA_FOLDER, name)):
        pcf_logger.info('Processing file {0}'.format(file))
        raw_data = []
        with open(os.path.join(config.GRAFANA_DATA_FOLDER, name, file), 'r', encoding='utf-8') as fr:
            csvR = csv.DictReader(fr)
            metadata = (file.replace('.csv', '')).split('_')
            regex = r"^((.*):\s([T|P|K]\w*\s\d*):\s(.*))|((.*):\s(.*):\s(.*))$"
            for item in csvR:
                record = {
                    'id': id,
                    'conta': metadata[0],
                    'perfil': metadata[1]
                }

                if item['Date']:
                    pts = item['Date'].split('/')
                    record['load_date'] = datetime.datetime(
                        int(pts[2]), int(pts[1]), int(pts[0]), 0, 0, 0)

                match = re.search(regex, item['Title'], re.MULTILINE)

                if match:
                    record['tipo'] = 'Série'
                    if match.group(1):
                        record['titulo'] = match.group(2)
                        record['temporada'] = match.group(3)
                        record['episodio'] = match.group(4)
                    else:
                        record['titulo'] = match.group(6)
                        record['temporada'] = match.group(7)
                        record['episodio'] = match.group(8)
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

        j = 1
        for item in raw_data:
            try:
                elem = NetflixViewHistory(**item)
                dbcon.add(elem)
                j += 1
                if j % 10 == 0:
                    dbcon.commit()
                    pcf_logger.info('Saved {0} records.'.format(j))
            except:
                pcf_logger.info(item)

        dbcon.commit()
        id += 1


if __name__ == "__main__":
    typer.run(load_data)
