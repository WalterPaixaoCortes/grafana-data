# -*- coding: utf-8 -*-
"""
    Process Survey Monkey Data
"""

import typer
import os
import csv
import time

from utils.GSheetWrapper import GSheetWrapper
from utils import config
from utils.pcf_logging import pcf_logger


# ---------------------------------------------------------------------------------------------------------------------
def save_to_gsheet(file_name, log, raw_data, save_json):
    gsheet = GSheetWrapper(config.GOOGLE_SVC_ACCOUNT)
    spreadsheet_id = gsheet.spreadsheet_exists(
        file_name.lstrip().rstrip(), config.GOOGLE_FOLDER)

    if not spreadsheet_id:
        log.info('creating spreadsheet {0}'.format(file_name))
        spreadsheet_id = gsheet.create_spreadsheet2(
            file_name.lstrip().rstrip(), config.GOOGLE_FOLDER)

    if save_json:
        with open(file_name.lstrip().rstrip()+'.json', 'w') as fw:
            fw.write(str(raw_data))

    for item in raw_data:
        log.info('Saving %s tab...' % item)
        data_parsed = []
        rows = []
        if len(raw_data[item]) > 0:
            for idx, row in enumerate(raw_data[item]):
                if idx == 0:
                    rows.append([cel for cel in row])
                rows.append([row[cel] for cel in row])

            i = 0

            log.info(
                'Starting data insertion of {0} rows of data...'.format(len(rows)))
            gsheet.populate_sheet(spreadsheet_id, item, {
                                  "values": rows[i:i+config.BATCH_SIZE]})
            i += config.BATCH_SIZE
            j = 0
            while i+config.BATCH_SIZE < len(rows):
                gsheet.append_sheet(spreadsheet_id, item, {
                                    "values": rows[i:i+config.BATCH_SIZE]})
                i += config.BATCH_SIZE
                log.info('{0} records inserted...'.format(i))
                j += 1
                if j == config.WAIT_INTERVAL:
                    j = 0
                    time.sleep(2)

            if i < len(rows):
                gsheet.append_sheet(spreadsheet_id, item, {"values": rows[i:]})


# ---------------------------------------------------------------------------------------------------------------------
def execute(name: str):
    with open(os.path.join(config.DATA_FOLDER, name), 'r', encoding='utf-8') as fr:
        pcf_logger.info('Loading from file...')
        csvR = csv.DictReader(fr)
        raw_data = []
        for item in csvR:
            raw_data.append(item)

        pcf_logger.info('Saving to Google...')
        save_to_gsheet(os.path.splitext(name)[0], pcf_logger, {
                       config.GOOGLE_TAB_NAME: raw_data}, False)


# ---------------------------------------------------------------------------------------------------------------------
# Main routine
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    typer.run(execute)
