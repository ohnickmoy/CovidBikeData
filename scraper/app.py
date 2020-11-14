"""Downloads Citibike trip data as zip files then unzips them.
Downloads NY trip data for January 2020 to previous published month
"""

import os
import zipfile
import json
import datetime
import calendar
import requests

def get_previous_month_with_year():
    """Checks for current month and returns the last month,
    since Citibike publishes data of a given month a month later
    ex. Data for January is published February
    Returns:
        tuple: Tuple of previous month and its associated year
    """

    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year = now.year if past_month != 12 else now.year - 1

    return (past_month, year)

def get_trip_data(json_file_path):
    """Takes in a file path (expected to be json) that contains
    information that corresponds to each monthlike URLs to files and file paths

    Args:
        json_file_path (string): string of filepath

    Returns:
        dict: dictionary of loaded data from JSON
    """
    try:
        with open(json_file_path) as json_file:
            trip_data = json.load(json_file)
    except IOError:
        print('Could not read file')

    return trip_data

def retrieve_citibike_data():

    """Retrieves trip data from Citibike's S3 buckets as zip files.
    Checks against trip_data json to see if anything new, and downloads it, add's it to repo
    Returns:
        Nothing
    """
    # open JSON_file
    json_file_path = './tripdata/trip_data.json'
    trip_data = get_trip_data(json_file_path)

    target = './tripdata/zip/citibike_tripdata_'

    # get current date to attempt get last months data
    # since data lags a month ie in October, expect a September data dump
    # make special case when current month is January

    past_month_with_year = get_previous_month_with_year()

    for month in range(1, 13):

        if month > past_month_with_year[0]:
            break

        date_format = str(past_month_with_year[1]) + '{:02d}'.format(month)
        if date_format not in trip_data:
            url = 'https://s3.amazonaws.com/tripdata/' + date_format + '-citibike-tripdata.csv.zip'

            # make request first. If 404, break loop, otherwise, continue with data download
            response = requests.get(url)

            if response.status_code == 404:
                print('404 status was issued.')
                print(f'Data for {calendar.month_name[past_month_with_year[0]]} not ready yet')
                break

            file_path = target + date_format + ".csv.zip"
            past_month_trip_json = {
                    'url': url,
                    'file_path': file_path
            }
            trip_data[date_format] = past_month_trip_json

            with open(file_path, 'wb') as opened_file:
                opened_file.write(response.content)

            print(str(past_month_with_year[1]) + "-" + str(month) + " done")

    print("Overwriting %s" % json_file_path)
    with open(json_file_path, "wt") as overwritten_file:
        json.dump(trip_data, overwritten_file, indent=4)


def unzip_citibike_data(zip_dir, csv_dir):

    """Unzips Citibike zip files for NY.
    Returns:
        Nothing
    """

    extension = ".zip"

    # for each zip file in zip_dir extract data to csv_dir
    for item in os.listdir(zip_dir):
        if item.endswith(extension):

            # create zipfile object and extract
            file_name = zip_dir + item
            print(file_name)
            with zipfile.ZipFile(file_name, "r") as zip_ref:
                zip_ref.extractall(csv_dir)
                print(item + " done")
                os.remove(file_name)

if __name__ == "__main__":
    retrieve_citibike_data()
    unzip_citibike_data("./tripdata/zip/", "./tripdata/csv/")
