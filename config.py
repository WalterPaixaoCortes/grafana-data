import os

GRAFANA_DATA_API_KEY = None
if 'API_KEY' in os.environ:
    API_KEY = os.environ['API_KEY']

GRAFANA_DATA_FOLDER = None
if 'GRAFANA_DATA_FOLDER' in os.environ:
    GRAFANA_DATA_FOLDER = os.environ['GRAFANA_DATA_FOLDER']

SEPARATOR = ','

DB_HOST = 'postgresql-22468-0.cloudclusters.net'
DB_SERVER = f'postgresql+psycopg2://wpcortes:Wrpc.1975@{DB_HOST}:22468/grafana'
DB_COMMIT_BATCH = 10
