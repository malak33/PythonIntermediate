import unittest
from ch08_testing.file_sizer import convert_file_size


class TestConvertFileSize(unittest.TestCase):

    def test_convert_file_size_standard(self):
        filesize = 1200
        expected = '1.2 KB'
        actual = convert_file_size(filesize)
        self.assertEqual(expected, actual)

    def test_convert_file_size_test_precision(self):
        filesize = 120000
        precision = 2
        expected = '117.19 KB'
        actual = convert_file_size(filesize, precision)
        self.assertEqual(expected, actual)

    def test_convert_file_size_test_override(self):
        filesize = 1234567890
        precision = 2
        units = 'MB'
        expected = '1,177.38 MB'
        actual = convert_file_size(filesize, precision, override=units)
        self.assertEqual(expected, actual)

    def test_convert_file_size_test_bad_input(self):
        with self.assertRaises(TypeError):
            convert_file_size('hello')


def main():
    unittest.main()

if __name__ == '__main__':
    main()