"""
    document.py  -   Module for the Document and DocumentManger classes

    Class module for our Document and DocumentManager classes.  This file is initially
    imported by task3_1.py and executed there.

    The Document class simply holds information about files.
    The DocumentManager is used to connect to and query (and eventually insert and delete records to/from)
    the documents.db sqlite3 database.
"""
from sqlite3 import connect, Row, Error


class Document:
    def __init__(self, filename, path, is_public, filesize, when_added):
        self.filename = filename
        self.path = path
        self.is_public = is_public
        self.filesize = filesize
        self.when_added = when_added

    def __str__(self):
        return '{fn}'.format(fn=self.filename)

    __repr__ = __str__


class DocumentManager:
    def __init__(self, db_file):
        self.tbl = 'documents'
        self.connection = connect(db_file)
        self.connection.row_factory = Row               # enable row names instead of indices
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def list_all(self):
        results = []
        try:
            self.cursor.execute('SELECT * FROM {tbl}'.format(tbl=self.tbl))
            for doc in self.cursor.fetchall():
                results.append(Document(doc['filename'], doc['path'], doc['is_public'],
                                        doc['filesize'], doc['when_added']))
        except Error as err:
            print('Error retrieving records: {err}'.format(err=err))
        return results

    def list_public(self):
        return [doc for doc in self.list_all() if doc.is_public]

    def retrieve(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass
