import gzip
import shutil
import requests
import os
import zipfile
import json
import datetime
import calendar

"""Downloads Citibike trip data as zip files then unzips them.
Downloads NY trip data for January 2020 to previous published month
"""

def retrieve_citibike_data():

    """Retrieves trip data from Citibike's S3 buckets as zip files.
    Checks against trip_data json to see if anything new, and downloads it, add's it to repo
    Returns:
        Nothing
    """
    # open JSON_file
    json_file_path = './tripdata/trip_data.json'
    try:
        with open(json_file_path) as json_file:
            trip_data = json.load(json_file)
    except IOError:
        print('Could not read file')

    target = './tripdata/zip/citibike_tripdata_'
    
    # get current date to attempt get last months data
    # since data lags a month ie in October, expect a September data dump
    # make special case when current month is January 

    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year = now.year if past_month != 12 else now.year - 1 
    
    for month in range(1, 13):

        if month > past_month:
            break

        date_format = str(year) + '{:02d}'.format(month)
    
        if date_format not in trip_data:
            url = 'https://s3.amazonaws.com/tripdata/' + date_format + '-citibike-tripdata.csv.zip'
            
            # make request first. If 404, break loop, otherwise, continue with data download
            r = requests.get(url)

            if r.status_code == 404:
                print(f'404 status was issued. Data for {calendar.month_name[past_month]} not ready yet')
                break

            file_path = target + date_format + ".csv.zip"
            past_month_trip_json = {
                    'url': url,
                    'file_path': file_path
            }
            trip_data[date_format] = past_month_trip_json

            with open(file_path, 'wb') as f:
                    f.write(r.content)

            print(str(year) + "-" + str(month) + " done")

    print("Overwriting %s" % json_file_path)
    with open(json_file_path, "wt") as fp:
        json.dump(trip_data, fp, indent=4)


def unzip_citibike_data():

    """Unzips Citibike zip files for NY.
    Returns:
        Nothing
    """

    zip_dir = "./tripdata/zip/"
    csv_dir = "./tripdata/csv/"
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
    unzip_citibike_data()
