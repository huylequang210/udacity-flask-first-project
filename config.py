import os

class Config(object):
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'free-db-huylq25.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'free-db-huylq25'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'huylequang210'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '%40Bondaica123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
