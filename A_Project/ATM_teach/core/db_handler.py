import json,time ,os
from conf import settings

def file_db_handle(conn_params):
    print('file db:', conn_params)
    return file_execute

def db_handler():
    conn_parmas=settings.DATABASE
    if conn_parmas['engine'] == 'file_storage':
        return file_db_handle(conn_parmas)
    elif conn_parmas['engine'] == 'mysql':
        pass

def file_execute(sql, **kwargs):
    conn_parmas = settings.DATABASE
    db_path = '%s%s'%()



























