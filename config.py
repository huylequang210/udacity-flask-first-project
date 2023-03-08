import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'huylqstore'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'hiqm8G5eUnNgr2bQcq62+93gncvfiJzpMgwGfm4nCrncxehOnZ6I6f4DUZKZZ/hl+Qo78a0B94eD+AStfokmbQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'free-db-huylq25.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'free-db-huylq25'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'huylequang210'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '%40Bondaica123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "AQr8Q~2dODSFuxrMmaGi8~DtNvRZkdfWCsFsRc87"

    AUTHORITY = "https://login.microsoftonline.com/9fbdf6f6-bf39-44b4-8a80-4d24a85affc9"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "d621d96d-0688-4073-8f3d-745397b4df4f"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session