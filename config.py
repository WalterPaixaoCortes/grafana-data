import os

GRAFANA_DATA_API_KEY = None
if 'API_KEY' in os.environ:
    API_KEY = os.environ['API_KEY']

GRAFANA_DATA_FOLDER = None
if 'GRAFANA_DATA_FOLDER' in os.environ:
    API_KEY = os.environ['GRAFANA_DATA_FOLDER']
