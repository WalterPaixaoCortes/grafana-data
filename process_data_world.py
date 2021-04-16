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

from models import Artigos
import requests
import json

from bs4 import BeautifulSoup

db.init()


def return_tag(text):
    keywords = ['visualization', 'data', 'dashboard', 'tableau', ]
    lst = text.split(' ')
    for item in lst:
        if item.replace(',', '').replace('.', '').replace('!', '').replace('?', '').lower() in keywords:
            return 'DataViz'
    return 'General'


def load_data(clean: str):
    urls = ['https://query.data.world/s/l7cerlwzlbzpqhpay3nzxetg6j6nac']

    raw_data = []

    root_folder = 'data//bookmarks'

    for root, _, files in os.walk(root_folder):
        for file_p in files:
            soup = BeautifulSoup(
                open(os.path.join(root_folder, file_p), 'r', encoding='utf-8'), 'html.parser')
            results = soup.find_all('li')
            for item in results:
                raw_data.append({'bookmarked_at': '2020-01-01T00:01:00', 'bookmarkedat': '2020-01-01T00:01:00',
                                 'post_url': item.a['href'], 'posturl': item.a['href'], 'post_title': item.a.text, 'posttitle': item.a.text})

    for url in urls:
        response = requests.get(url)

        raw_articles = response.text.split('\n')

        for item in raw_articles:
            try:
                raw_item = json.loads(item)
                raw_data.append(raw_item)
            except:
                print(item)

    pcf_logger.info('Removing duplicates...')
    r_data = {each['post_title']: each for each in raw_data}.values()

    pcf_logger.info('Saving into database...')
    dbcon = db.get_db()

    if clean.upper() == 'SIM':
        dbcon.query(Artigos).delete()

    j = 1
    for item in r_data:
        try:
            elem = Artigos()
            elem.id = j
            elem.titulo = item['post_title']
            elem.url = item['post_url']
            elem.data = item['bookmarked_at']
            elem.tag = return_tag(item['post_title'])
            dbcon.add(elem)
            j += 1
            if j % 10 == 0:
                dbcon.commit()
                pcf_logger.info('Saved {0} records.'.format(j))
        except:
            pcf_logger.info(item)

    dbcon.commit()


if __name__ == "__main__":
    typer.run(load_data)
