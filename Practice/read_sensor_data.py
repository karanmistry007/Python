import csv
from datetime import datetime, timedelta


def unix_to_ist(unix_time):
    utc_time = datetime.utcfromtimestamp(unix_time)
    ist_offset = timedelta(hours=5, minutes=30)  # IST offset is UTC+5:30
    parts = utc_time + ist_offset
    return parts


# Read data from the long multi-line text file
txt_file_path = "sensors.log"
csv_file_path = "data.csv"

headers = [
    "Type",
    "sensor_id",
    "temprature_1",
    "temprature_2",
    "temprature_3",
    "temprature_4",
    "temprature_5",
    "humidity_1",
    "humidity_2",
    "humidity_3",
    "co_1",
    "TimeStamp",
]
data = []  # To store data for writing to CSV

# Open the text file and process its lines
with open(txt_file_path, "r") as txt_file:
    for line in txt_file:
        line = line.strip()  # Remove leading/trailing whitespace
        values = line.split(",")  # Split line by comma or your delimiter

        processed_values = []  # To store values processed after splitting

        for value in values:
            parts = value.split(" ")
            for part in parts:
                newp = part.split("=")
                processed_values.extend(newp)

                # remove unwanted fields
                for temp in processed_values:
                    if temp == "sensor_id":
                        processed_values.remove("sensor_id")

                for temp in processed_values:
                    if temp == "temperature":
                        processed_values.remove("temperature")

                for temp in processed_values:
                    if temp == "humidity":
                        processed_values.remove("humidity")

                for temp in processed_values:
                    if temp == "co":
                        processed_values.remove("co")

                # for UNIX to IST Convertion
                for temp in processed_values:
                    if "0000000000" in temp:
                        # print("yes")
                        unix_time = temp[0:9]
                        unix_time = int(unix_time)
                        processed_values.remove(temp)
                        ist_time = unix_to_ist(unix_time)
                        processed_values.append(ist_time)

        data.append(processed_values)
        # print(data)

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerows(data)


print("CSV file has been created.")

# csv_file_path = 'data.csv'  # Replace with the path to your CSV file

# seventh_column = []  # List to store values from the 7th column
# time_list=[]

# with open(csv_file_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         if len(row) >= 12:
#             seventh_column.append(row[11])  # Index 6 corresponds to the 7th column (0-based index)
#             for temp in seventh_column:
#                 # print(temp)
#                 temp=temp[0:10]
#                 temp=int(temp)
#                 time=unix_to_ist(temp)
#                 print(time)
#                 time_list.append(time)
#                 # print(time_list)
