# -*- coding: utf-8 -*-
'''Login blueprint views. Contains routes regarding authentication'''
from sqlalchemy import func, and_, desc, asc
from pcf_logging import pcf_logger
import config
import database as db
from models import IMDBMovies
import csv
import os
import typer


def only_number(val):
    ret = ''
    for item in val:
        if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ret += item
    return ret


def load_data(name: str):
    pcf_logger.info('Loading IMDB Movies...')
    cnx = db.get_db()

    with open(os.path.join(config.DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        csvR = csv.DictReader(fr)
        max = cnx.query(
            func.count(IMDBMovies.imdb_title_id)).scalar()
        if max is None:
            max = 0

        i = 0
        m = 0
        for item in csvR:
            if m >= max:
                if item['budget'] == '':
                    item['budget'] = 0
                else:
                    item['budget'] = float(only_number(item['budget']))

                if item['usa_gross_income'] == '':
                    item['usa_gross_income'] = 0
                else:
                    item['usa_gross_income'] = float(
                        only_number(item['usa_gross_income']))

                if item['worlwide_gross_income'] == '':
                    item['worlwide_gross_income'] = 0
                else:
                    item['worlwide_gross_income'] = float(
                        only_number(item['worlwide_gross_income']))

                if item['metascore'] == '':
                    item['metascore'] = 0

                if item['reviews_from_users'] == '':
                    item['reviews_from_users'] = 0

                if item['reviews_from_critics'] == '':
                    item['reviews_from_critics'] = 0

                date_parts = item['date_published'].split('-')
                if len(date_parts) <= 1:
                    item['date_published'] = date_parts[0] + '-01-01'

                rec = IMDBMovies(**item)
                cnx.add(rec)

            i += 1
            m += 1
            if i == 100:
                i = 0
                cnx.commit()
                pcf_logger.info('{0} records saved.'.format(m))

        cnx.commit()

    pcf_logger.info('Loading IMDB Movies is done...')


if __name__ == '__main__':
    pcf_logger.info('Connecting to database...')
    db.init()
    typer.run(load_data)
    pcf_logger.info('Closing the database...')
    db.close()
