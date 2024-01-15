"""

This module creates the classes for the student simulator.
I will create 8 classes with 50 students each.

"""
import random
import csv
import os


# Read the names from the files
try:
    with open("student_simulator/BoyNames.txt", 'r') as boys:
        boy_names = boys.read().splitlines()
    with open("student_simulator/GirlNames.txt", 'r') as girls:
        girl_names = girls.read().splitlines()
except FileExistsError:
    print("File does not exist")
    exit(1)
except Exception as e:
    print(e)
    exit(1)
names = boy_names + girl_names

# Randomize the name to create classes with csv files
classes = ["10A", "10B", "10C", "10D", "10E", "10F", "10G", "10H"]
class_counter = 0
id_counter = 0

while names:
    header = [['Name', 'ID']]
    data = []

    while True:
        id_counter += 1
        data.append([names.pop(random.randint(0, len(names) - 1)), str(id_counter)])
        if id_counter % 50 == 0:
            break

    data.sort(key=lambda x: x[0])

    os.makedirs(f"classes", exist_ok=True)

    csv_file = open(f"classes/Class {classes[class_counter]}.csv", 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(header + data)
    csv_file.close()
    
    class_counter += 1
