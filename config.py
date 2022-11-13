import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sreesqldba.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'SreeSQLDB'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'adminsree'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Summer@12345'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storagesree1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'mn/9ZdwGvBmFed57FKZu+NdhI9NpVGf5Xy7qhdyIEphnZ3ye2JzzvMAmffekphft4rIHivfS/KRf+AStobOwpQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
