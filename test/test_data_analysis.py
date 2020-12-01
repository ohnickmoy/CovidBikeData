"""Test suite for data_analysis.py
"""

import unittest
import os
from plotdata import data_analysis

class TestDataAnalysis(unittest.TestCase):
    """Class testing suite for data_analysis.py
    """
    def test_get_csv_file_paths(self):
        """Test for get_csv_file_paths, which takes in a file path
        to get csvs. Assumes files are in the path and csvs are there
        """
        test_path = "./test/testfiles/csvs/"
        path_results = data_analysis.get_csv_file_paths(test_path)

        self.assertEqual(len(path_results), 2)

    def test_generate_total_ridership_data(self):
        """Test for generate_total_ridership_data. Takes in filepaths from
        get_csv_file_paths and a directory.
        """

        test_path = "./test/testfiles/csvs/"
        test_csv_file_paths = data_analysis.get_csv_file_paths(test_path)

        self.assertEqual(len(test_csv_file_paths), 2)

        test_ridership_data = data_analysis.generate_total_ridership_data(test_csv_file_paths,
                                                                          test_path)

        self.assertEqual(bool(test_ridership_data.get('year_months')), True)
        self.assertEqual(bool(test_ridership_data.get('total_trips_per_month')), True)

        self.assertEqual(len(test_ridership_data['year_months']), 2)
        self.assertEqual(len(test_ridership_data['total_trips_per_month']), 2)

    def test_generate_total_ridership_chart(self):
        """Test to generate chart of total ridership
        """

        test_path = "./test/testfiles/csvs/"
        test_csv_file_paths = data_analysis.get_csv_file_paths(test_path)

        test_ridership_data = data_analysis.generate_total_ridership_data(test_csv_file_paths,
                                                                          test_path)

        test_image_file_path = './test/testfiles/images/test_image_2.png'

        data_analysis.generate_total_ridership_chart(test_ridership_data, test_image_file_path)
        image_paths = os.listdir('./test/testfiles/images/')

        self.assertEqual(len(image_paths), 2)
        assert 'test_image_2.png' in image_paths

if __name__ == "__main__":
    unittest.main()
