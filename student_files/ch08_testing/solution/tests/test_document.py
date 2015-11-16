import unittest
from ch08_testing.solution.document import DocumentManager, Document


class TestDocumentManager(unittest.TestCase):

    def setUp(self):
        db_file = '../../../resources/documents.db'
        self.docMgr = DocumentManager(db_file)

    def test_retrieve_valid_query(self):
        expected = Document('sample.txt', '', 1, 70, 'May 18 2015 04:34PM')
        actual = self.docMgr.retrieve('sample.txt')
        self.assertIsInstance(actual, Document)
        self.assertEqual(expected.filename, actual.filename)
        self.assertEqual(expected.path, actual.path)
        self.assertEqual(expected.is_public, actual.is_public)
        self.assertEqual(expected.filesize, actual.filesize)
        self.assertEqual(expected.when_added, actual.when_added)

    def test_retrieve_wrong_input(self):
        actual = self.docMgr.retrieve('foo')
        self.assertIsNone(actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()