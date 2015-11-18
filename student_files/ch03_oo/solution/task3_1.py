"""
    task3_1.py  -   document listing test file

    This file serves as a driver to test the DocumentManager class found
    within document.py.
    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.
"""
#mark ch03_oo/solution as the doc root
from document import DocumentManager

database = '../../resources/documents.db'

def do_work():
    doc_mgr = DocumentManager(database)
    print(doc_mgr.list_public())

do_work()

