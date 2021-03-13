# -*- coding: utf-8 -*-
'''Login blueprint views. Contains routes regarding authentication'''
import csv
import os
import typer
import traceback

from sqlalchemy import func, and_, desc, asc

from models import BrasileiraoStats, Brasileirao, FilmesBrasil
from pcf_logging import pcf_logger
import config
import database as db


def only_number(val):
    ret = ''
    for item in val:
        if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ret += item
    return ret


def load_filmes_brasil(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(FilmesBrasil).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            record = FilmesBrasil(**item)
            cnx.add(record)
            i += 1
            m += 1
            if i == config.DB_COMMIT_BATCH:
                cnx.commit()
                pcf_logger.info(
                    '{0} records added to {1} table.'.format(m, table_name))
                i = 0

        cnx.commit()
        pcf_logger.info('Data loaded into {0}...'.format(table_name))


def load_brasileirao(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(Brasileirao).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            record = Brasileirao(**item)
            cnx.add(record)
            i += 1
            m += 1
            if i == config.DB_COMMIT_BATCH:
                cnx.commit()
                pcf_logger.info(
                    '{0} records added to {1} table.'.format(m, table_name))
                i = 0

        cnx.commit()
        pcf_logger.info('Data loaded into {0}...'.format(table_name))


def load_brasileirao_stats(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(BrasileiraoStats).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            if '%' in item['posse_bola']:
                item['posse_bola'] = float(item['posse_bola'].replace('%', ''))
            else:
                if item['posse_bola']:
                    item['posse_bola'] = float(item['posse_bola'])

            if '%' in item['precisao_passe']:
                item['precisao_passe'] = float(
                    item['precisao_passe'].replace('%', ''))
            else:
                if item['precisao_passe']:
                    item['precisao_passe'] = float(item['precisao_passe'])

            record = BrasileiraoStats(**item)
            cnx.add(record)
            i += 1
            m += 1
            if i == config.DB_COMMIT_BATCH:
                cnx.commit()
                pcf_logger.info(
                    '{0} records added to {1} table.'.format(m, table_name))
                i = 0

        cnx.commit()
        pcf_logger.info('Data loaded into {0}...'.format(table_name))


def load_data(name: str):
    pcf_logger.info('Connecting to database...')
    db.init()
    pcf_logger.info('Starting data into grafana database...')
    try:
        fn_name = os.path.splitext(name)[0]
        fn = eval('load_{0}'.format(fn_name))
        fn(name, fn_name)
    except:
        pcf_logger.info(
            '{0} file or {1} function were not available for the load...'.format(name, fn_name))
        pcf_logger.info(traceback.format_exc())

    pcf_logger.info('Finishing data into grafana database...')
    pcf_logger.info('Closing the database...')
    db.close()


if __name__ == '__main__':
    typer.run(load_data)
