"""
    create_documents_db.py  -   documents database creation script

    This file is used with the Document database (documents.db).  It is used to create
    (or re-create) the documents.db file in the student_files/resources directory.
    If you wish to restore the database, simply delete documents.db and run this script again.

    NOTE!!!:
    This script should not have to be run as the files and database are already created.

"""
import sqlite3
from datetime import datetime

database_file = '../../resources/documents.db'
table_name = 'documents'
id_col = 'document_id'
filename_col = 'filename'
path_col = 'path'
filesize_col = 'filesize'
is_public_col = 'is_public'
when_added_col = 'when_added'


DROP_SQL = 'DROP TABLE IF EXISTS {tbl}'.format(tbl=table_name)
CREATE_SQL = 'CREATE TABLE IF NOT EXISTS {tbl} ' \
             '({id} INTEGER PRIMARY KEY AUTOINCREMENT, ' \
             '{fn} TEXT, ' \
             '{path} TEXT, ' \
             '{filesz} INTEGER, ' \
             '{when_added} TEXT, ' \
             '{ispub} INTEGER)' \
             .format(tbl=table_name,
                     id=id_col,
                     fn=filename_col,
                     path=path_col,
                     filesz=filesize_col,
                     when_added=when_added_col,
                     ispub=is_public_col)


document_data = [
    (1, 'sample.txt', '', 70, datetime.now().strftime('%B %d %Y %I:%M%p'), 1),
    (2, 'sample2.txt', '', 135, datetime.now().strftime('%B %d %Y %I:%M%p'), 0),
    (3, 'sample3.txt', '', 40, datetime.now().strftime('%B %d %Y %I:%M%p'), 1)
]

connection = None
try:
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(DROP_SQL)
    cursor.execute(CREATE_SQL)
    cursor.executemany('INSERT INTO {tbl}({id}, {fn}, {path}, {filesz}, {when_added}, {ispub}) VALUES (?,?,?,?,?,?)'
                       .format(tbl=table_name,
                               id=id_col,
                               fn=filename_col,
                               path=path_col,
                               filesz=filesize_col,
                               when_added=when_added_col,
                               ispub=is_public_col),
                       document_data)
    connection.commit()
    print('Data loaded into documents table')
except sqlite3.Error as e:
    connection.rollback()
    print('Data not loaded into documents table')
    print('Error: {0}'.format(e))
finally:
    if connection:
        connection.close()
