import unittest
import code
import datetime
from unittest import mock
from code import app

class TestApp(unittest.TestCase):
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


if __name__ == "__main__":
   unittest.main() 