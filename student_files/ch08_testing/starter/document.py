"""
    document.py  -   Module for the Document and DocumentManger classes

    Class module for our Document and DocumentManager classes.  This file will be utilized by
    the server.py XMLRPC module.

    The Document class simply holds information about files.
    The DocumentManager is used to connect to and query (and eventually insert and delete records to/from)
    the documents.db sqlite3 database.
"""
from datetime import datetime
import sqlite3
from sqlite3 import connect, Row
from ch08_testing.starter.support.logger import log


class Document:
    def __init__(self, filename, path, is_public, filesize, when_added):
        self.filename = filename
        self.path = path
        self.is_public = is_public
        self.filesize = filesize
        self.when_added = when_added

    def __str__(self):
        return '{0}'.format(self.filename)

    __repr__ = __str__


class DocumentManager:
    def __init__(self, db_file='../../resources/documents.db'):
        self.connection = connect(db_file)
        self.connection.row_factory = Row               # enable row names instead of indices
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    @log
    def list_all(self):
        results = []
        self.cursor.execute('SELECT * FROM {tbl}'.format(tbl='documents'))
        for doc in self.cursor.fetchall():
            results.append(Document(doc['filename'], doc['path'], doc['is_public'], doc['filesize'], doc['when_added']))
        return results

    @log
    def list_public(self):
        return [doc for doc in self.list_all() if doc.is_public]

    @log
    def retrieve(self, filename):
        pass

    @log
    def add(self, filename, path='', is_public=False, filesize=0, when_added=datetime.now()):
        results = False
        try:
            d = Document(filename, path, is_public, filesize, when_added.strftime('%B %d %Y %I:%M%p'))

            self.cursor.execute('INSERT INTO {tbl}({fn}, {path}, {filesz}, {when_added}, {ispub}) VALUES (?,?,?,?,?)'
                                .format(tbl='documents', fn='filename', path='path',
                                        filesz='filesize', when_added='when_added', ispub='is_public'),
                                (d.filename, d.path, d.filesize, d.when_added, d.is_public))

            self.connection.commit()
            results = True
        except sqlite3.Error:
            pass

        return results

    def remove(self, filename):
        results = False
        try:
            file_delete_sql = 'DELETE FROM {tbl} WHERE {column}="{value}"'.format(tbl='documents', column='filename', value=filename)
            results = self.cursor.execute(file_delete_sql)
            self.connection.commit()
        except sqlite3.Error:
            pass

        return results.rowcount
