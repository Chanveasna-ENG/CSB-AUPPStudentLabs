"""
This file is used to generate random web log 
Parameters: Name, ID, Timestamp, URL, Time Spent
"""
import random
from datetime import datetime, timedelta
import csv
import os


classes_dir = "classes"


def get_random_date(start_date, end_date):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    random_hour = random.randrange(24)
    random_minute = random.randrange(60)
    random_second = random.randrange(60)
    random_date = random_date + timedelta(hours=random_hour, minutes=random_minute, seconds=random_second)

    return random_date


def read_csv(csv_file):
    with open(f"{classes_dir}/{csv_file}", 'r') as students:
        reader = csv.reader(students)
        next(reader)
        return [row for row in reader]


def write_to_csv(header, data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(header + data)


def list_files(dir):
    try:
        return [file for file in os.listdir(dir) if file.endswith(".csv")]
    except FileExistsError:
        print("File does not exist")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)


csv_files = list_files(classes_dir)
if csv_files == []:
    print("No classes found")
    exit(1)

for i in range(1, 3):
    data = []
    for csv_file in csv_files:
        data += read_csv(csv_file)
    
    new_data = []
    for _ in range(6969):
        student = data[random.randint(0, len(data) - 1)]
        new_data.append([get_random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime("%Y-%m-%d %H:%M:%S"),student[0], student[1], "www.myschool.com", random.randint(0, 120)])
    
    new_data.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"), reverse=True)

    os.makedirs(f"semester {i}", exist_ok=True)
    write_to_csv(
        header=[['Timestamp', 'Name', 'ID', 'URL', 'Time Spent']], 
        data=new_data, 
        file_name=f"semester {i}/web log.csv"
    )
