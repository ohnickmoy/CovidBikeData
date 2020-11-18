"""Takes in data downloaded from scraper/app.py and does some ploting of data
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# def open_csvs(csv_dir):
#     trip_csvs = os.listdir(csv_dir)
#     pass
# df = pd.read_csv('./tripdata/csv/202003-citibike-tripdata.csv')

# pd.set_option('display.max.columns', None)
# # print(df.head())
# # if __name__ == "__main__":
#     # trip_dir = "./tripdata/csv/"
#     #open_csvs(trip_dir)
#     # print(os.listdir(trip_dir))
# print(len(df.index))
# print(df['usertype'].value_counts())
# # df['usertype'].value_counts().plot(kind='bar')
# plt.plot(['202003', '202004', '202005'], [23, 28, 35])
# plt.show()

"""get the trip_csvs
    parse out their names, since it's uniform, split them, get the first one
    append it to the year month combos
    read the csv with trip_dir + file name
    append len of index to indexCounts
    plot and show
"""
TRIP_DIR = "./tripdata/csv/"
trip_csvs = os.listdir(TRIP_DIR)
trip_csvs.sort()
year_months = []
total_trips_per_month = []
for file_name in trip_csvs:
    file_list = file_name.split("-")
    year_month = file_list[0]
    print(f"Checking {year_month}")

    year_months.append(year_month)

    curr_file_path = TRIP_DIR + file_name
    df = pd.read_csv(curr_file_path)
    total_trips_per_month.append(len(df.index))

graph = plt.figure(figsize=(10, 6))
plt.plot(year_months, total_trips_per_month)

plt.show()
