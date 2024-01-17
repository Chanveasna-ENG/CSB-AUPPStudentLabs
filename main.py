import os
from schoolfilesystem import SchoolAssessmentSystem

classes_dir = "semester 1"
classes_dir2 = "semester 2"

try:
    csv_files = [file for file in os.listdir(classes_dir) if file.endswith(".csv") and file.startswith("Class")]
    csv_files2 = [file for file in os.listdir(classes_dir2) if file.endswith(".csv") and file.startswith("Class")]
except FileExistsError:
    print("File does not exist")
    exit(1)
except Exception as e:
    print(e)
    exit(1)

if csv_files == []:
    print("No classes found")
    exit(1)

SchoolAssessmentSystem(csv_files, web_log='https://raw.githubusercontent.com/Chanveasna-ENG/CSB-AUPPStudentLabs/main/semester%201/web%20log.csv', parent=classes_dir).generate_summary()
SchoolAssessmentSystem(csv_files2, web_log='https://raw.githubusercontent.com/Chanveasna-ENG/CSB-AUPPStudentLabs/main/semester%202/web%20log.csv', parent=classes_dir2).generate_summary()