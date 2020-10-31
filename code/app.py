import gzip
import shutil
import requests
import os
import zipfile

"""Downloads Citibike trip data as zip files then unzips them.
Downloads NY trip data for October 2019 to October 2020
"""

def retrieve_citibike_data():

    """Retrieves trip data from Citibike's S3 buckets as zip files.
    Downloads trip data from October 2010 to October 2020
    Returns:
        Nothing
    """

    target = "./tripdata/zip/citibike_tripdata_"
    year = 2020
    for month in range(1, 13):

        if month > 9:
            break

        date_format = str(year) + '{:02d}'.format(month)

        # retrieve data from citibike's s3 buckets and store in zip directory
        url = "https://s3.amazonaws.com/tripdata/" + date_format + "-citibike-tripdata.csv.zip"
        filePath = target + date_format + ".csv.zip"
        r = requests.get(url)

        with open(filePath, 'wb') as f:
                f.write(r.content)

        print(str(year) + "-" + str(month) + " done")


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
                #os.remove(file_name)


if __name__ == "__main__":
    # retrieve_citibike_data()
    # retrieve_citibike_jc_data()
    unzip_citibike_data()