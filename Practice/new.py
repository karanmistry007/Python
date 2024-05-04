import csv
from datetime import datetime, timedelta


def unix_to_ist(temp):
    utc_time = datetime.utcfromtimestamp(temp)
    ist_offset = timedelta(hours=5, minutes=30)  # IST offset is UTC+5:30
    parts = utc_time + ist_offset
    return parts


# Read data from the long multi-line text file
txt_file_path = "sensors.log"
csv_file_path = "data.csv"

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

        data.append(processed_values)

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
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
