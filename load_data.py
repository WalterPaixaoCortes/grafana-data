# -*- coding: utf-8 -*-
'''Login blueprint views. Contains routes regarding authentication'''
import csv
import os
import typer
import traceback

from sqlalchemy import func, and_, desc, asc

from models import BrasileiraoStats, Brasileirao, FilmesBrasil, ImdbMovies, Netflix, Perfil, Quadrante, Combustivel, VendaLivros
from pcf_logging import pcf_logger
import config
import database as db


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
            for key in item:
                if item[key] == '':
                    item[key] = None

            if item['publico_ano_exibicao']:
                item['publico_ano_exibicao'] = int(
                    float(item['publico_ano_exibicao']))
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
            for key in item:
                if item[key] == '':
                    item[key] = None

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
            for key in item:
                if item[key] == '':
                    item[key] = None

            if item['posse_bola'] and '%' in item['posse_bola']:
                item['posse_bola'] = float(item['posse_bola'].replace('%', ''))
            else:
                if item['posse_bola']:
                    item['posse_bola'] = float(item['posse_bola'])

            if item['precisao_passe'] and '%' in item['precisao_passe']:
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


def load_netflix(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(Netflix).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None

            item['id'] = item['id'].replace('s', '')

            record = Netflix(**item)
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


def load_perfil(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(Perfil).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None

            record = Perfil(**item)
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


def load_quadrante(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(Quadrante).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None

            item['id'] = m

            record = Quadrante(**item)
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


def load_combustivel(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(Combustivel).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr, delimiter=';')
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None
                else:
                    if key == 'data':
                        parsed_date = item[key].split('/')
                        item[key] = f'{parsed_date[2]}/{parsed_date[1]}/{parsed_date[0]}'
                    else:
                        item[key] = item[key].replace(',', '.')

            item['id'] = m

            record = Combustivel(**item)
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


def load_venda_livros(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        cnx.query(VendaLivros).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None

            item['id'] = m

            record = VendaLivros(**item)
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


def load_imdb_movies(name, table_name):
    with open(os.path.join(config.GRAFANA_DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Getting database conn...')
        cnx = db.get_db()

        pcf_logger.info('Finding id''s from {0} table...'.format(table_name))
        raw_already_saved = cnx.query(ImdbMovies).count()
        pcf_logger.info('Records = {0}...'.format(raw_already_saved))

        #pcf_logger.info('Deleting data from {0} table...'.format(table_name))
        # cnx.query(ImdbMovies).delete()

        pcf_logger.info('Loading rows...')
        csvR = csv.DictReader(fr)
        i = 0
        m = 0
        for item in csvR:
            for key in item:
                if item[key] == '':
                    item[key] = None

            m += 1
            if m > raw_already_saved:
                i += 1
                record = ImdbMovies(**item)
                cnx.add(record)
                if i == config.DB_COMMIT_BATCH:
                    try:
                        cnx.commit()
                    except:
                        cnx.rollback()
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
