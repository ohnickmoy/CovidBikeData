"""Test suite for app.py
"""
import unittest
import datetime
import os
from unittest import mock
from code import app

class TestApp(unittest.TestCase):
    """Class for testing suit for app.py
    """
    @mock.patch('datetime.datetime')
    def test_get_previous_month_with_year(self, mock_date):
        """Test for get_previous_month_with_year
        Since Citibike publishes data for a given month the following month, check that previous
        month is returned

        Args:
            mock_date (mock): mock object from the patch decorator that replaces datetime.datetime
            within get_previous_month_with_year
        """
        mock_date.now.return_value = datetime.date(2020, 11, 20)

        test_date = app.get_previous_month_with_year()

        self.assertEqual(test_date[0], 10)
        self.assertEqual(test_date[1], 2020)

    @mock.patch('datetime.datetime')
    def test_get_previous_month_when_january(self, mock_date):
        """Test for get_previous_month_with year, specially to test for January
        Since Citibike publishes data for a given month the following month, then for the month
        of January, it should be December of the previous year

        Args:
            mock_date (mock): mock object from the patch decorator that replaces datetime.datetime
            within get_previous_month_with_year
        """
        #set up mock datetime
        mock_date.now.return_value = datetime.date(2021, 1, 20)

        test_date = app.get_previous_month_with_year()

        self.assertEqual(test_date[0], 12)
        self.assertEqual(test_date[1], 2020)

    def test_get_trip_data(self):
        """Test for get_trip_data, which opens JSON file
        """
        test_path = "./test/test_json.json"
        test_results = app.get_trip_data(test_path)

        self.assertEqual(len(test_results),3)

    def test_unzip_data(self):
        """Test for unziping method.
        Checks to see if unzipping is successful in given file path
        """

        zip_dir = "./test/testfiles/zip/"
        fake_csv_dir = "./test/testfiles/text/"

        patcher = mock.patch('os.remove')
        patcher.start()

        app.unzip_citibike_data(zip_dir, fake_csv_dir)
        self.assertEqual(len(os.listdir(fake_csv_dir)), 4)

        patcher.stop()
        os.remove(f'{fake_csv_dir}test_txt4.txt')


if __name__ == "__main__":
    unittest.main()
