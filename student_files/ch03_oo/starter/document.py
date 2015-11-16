"""
    document.py  -   Module for the Document and DocumentManger classes

    Class module for our Document and DocumentManager classes.  This file is initially
    imported by task3_1.py and executed there.

    The Document class simply holds information about files.
    The DocumentManager is used to connect to and query
    (and eventually insert and delete records to/from)
    the documents.db sqlite3 database.

    -------------------------------------------------------------------------

    Helpful Hints:
    1. Create the Document class with the following attributes:
        filename, path, is_public, filesize, and when_added

    2. In the __init__, pass in parameters for each and set them as instance attributes


    -------


    3. Create the DocumentManager class beneath Document with the following methods:
        __init__, __del__, list_all, list_public, retrieve, add, remove

        Remember each method should have a self passed in.

        For now, just put pass in the body of each method.


    4. In the __init__(), pass in the path/filename for documents.db.


    5. Create a connection and cursor as follows:
        self.connection = sqlite3.connect(db_filename)
        self.connection.row_factory = Row
        self.cursor = self.connection.cursor()

        Don't forget to import sqlite3

        The constructor is finished.


    6. Implement the list_all() method.
       Create a list to return (this will be a list of Document objects).
       Using the DocumentManager's cursor object (self.cursor), invoke the execute() method.

       You may use the following sql:     'SELECT * FROM {tbl}'.format(tbl='documents')

       Now iterate over the cursor retrieving all records.  Add to the return object
       a Document object for each record retrieved.
       You should have something like this (careful!--your Document constructor may vary)
               for doc in self.cursor.fetchall():
                    results.append(Document(doc['filename'], doc['path'], doc['is_public'],
                                            doc['filesize'], doc['when_added']))

       Don't forget to return the list of Document objects.


    7. Implement the list_public() method.  This method can call list_all() but
       then simply iterates through all the records and remove any that are not public files.
       There are a couple of ways to do this.  One is to use a list comprehension.  Do you
       think you can use a list comprehension here.  If not, use a for loop and simply build
       a new list with non-public documents removed.  (Hint: check the Document's is_public property).

    8. Implement the destructor:  __del__().  This function will have one line
       to close the connection object.  Can you do this on your own?

    9. Leave retrieve(), add(), and remove() empty for now (just a pass statement in them)
       Return to the task3_1_starter.py file to finish the do_work() method
"""

