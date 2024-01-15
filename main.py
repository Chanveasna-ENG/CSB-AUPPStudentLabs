import os
from schoolfilesystem import SchoolAssessmentSystem

classes_dir = "semester 2"

try:
    csv_files = [file for file in os.listdir(classes_dir) if file.endswith(".csv") and file.startswith("Class")]
except FileExistsError:
    print("File does not exist")
    exit(1)
except Exception as e:
    print(e)
    exit(1)

if csv_files == []:
    print("No classes found")
    exit(1)

SchoolAssessmentSystem(csv_files, classes_dir, ).generate_summary()