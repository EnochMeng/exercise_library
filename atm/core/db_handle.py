##interactive process with database
import os
def file_db_handler(DATABASE):
    db_path = os.path.join(DATABASE['path'],'account')
    return db_path

def mysql_db_handler(DATABASE):
    pass


def db_handler(DATABASE):
    if DATABASE['engineer']=='file':
        return file_db_handler(DATABASE)
    elif DATABASE['engineer']=='mysql':
        return mysql_db_hander(DATABASE)
