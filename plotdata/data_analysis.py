"""Takes in data downloaded from scraper/app.py and does some ploting of data
"""
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def get_csv_file_paths(csv_dir):
    """takes in a file path to get files within a given directory
    and sorts them in alpha-numerical order

    Args:
        csv_dir (string): string of a given file path

    Returns:
        list: sorted list of files in a directory
    """
    csv_paths = os.listdir(csv_dir)
    csv_paths.sort()

    return csv_paths

def generate_total_ridership_data(csv_paths_list, csv_dir):
    """Generates data for total ridership of Citibike service during Covid-19 period

    Args:
        csv_paths_list (list): list of csv paths
        csv_dir (string): string of directory where csvs are located

    Returns:
        dict: dictionary of ridership data
    """
    year_months = []
    total_trips_per_month = []

    #traverse through the files in the trip_csv dir
    for file_name in csv_paths_list:
        file_list = file_name.split("-")
        year_month = file_list[0]
        print(f"Checking {year_month}")
        datetime_obj = datetime.datetime.strptime(year_month[4:], "%m")
        month_name = datetime_obj.strftime("%b")
        year_months.append(f"{month_name} {year_month[:4]}")

        curr_file_path = csv_dir + file_name
        data_file = pd.read_csv(curr_file_path)
        total_trips_per_month.append(len(data_file.index))

    total_ridership_data = {
        'year_months': year_months,
        'total_trips_per_month': total_trips_per_month
    }

    return total_ridership_data

def generate_total_ridership_chart(total_ridership_data):
    """Generates chart for total Citibike ridership during period of Covid-19

    Args:
        total_ridership_data (dictionary): dictionary containing corresponding ridership
        to given month and year
    """
    year_months = total_ridership_data['year_months']
    total_trips_per_month = total_ridership_data['total_trips_per_month']
    plt.figure(figsize=(11, 6))
    plt.plot(year_months, total_trips_per_month)
    plt.title(f"Citibike Ridership - {year_months[0]} to {year_months[len(year_months) - 1]}")
    plt.xlabel("Month and Year")
    plt.ylabel("Ridership in Millions")

    plt.savefig('./plotdata/images/covid_ridership.png')

if __name__ == '__main__':
    CSV_PATH = './tripdata/csv/'
    trip_csv_paths = get_csv_file_paths(CSV_PATH)
    all_ridership_data = generate_total_ridership_data(trip_csv_paths, CSV_PATH)
    generate_total_ridership_chart(all_ridership_data)
