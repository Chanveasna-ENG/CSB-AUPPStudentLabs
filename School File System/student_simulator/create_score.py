"""
This file is used to generate random score for students in each class.
full score is 100 for each subject.
Grade A = 90% and above (Excellent)
Grade B = 80% (Good)
Grade C = 70% (Average)
Grade D = 60% (Below Average)
Grade F = 50% and below (Fail)

5 student score(80-100)
20 student score (70-90)
20 student score (60-85)
5 student score (30-75)

10 subjects in total
Math Physics Chemistry Biology English History Geography Literature Philosophy Art
"""
import random
import csv
import os


script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.join(script_dir, "..")
class_dir = os.path.join(parent_dir, "classes") 
# Read the names from the files
try:
    csv_files = [file for file in os.listdir(class_dir) if file.endswith(".csv")]
except FileExistsError:
    print("File does not exist")
    exit(1)
except Exception as e:
    print(e)
    exit(1)

if csv_files == []:
    print("No classes found")
    exit(1)

for i in range(1, 3):
    for csv_file in csv_files:
        header = [['Name', 'ID', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Literature', 'Philosophy', 'Art']]
        data = []
        
        with open(os.path.join(class_dir, f"{csv_file}"), 'r') as students:
            reader = csv.reader(students)
            next(reader)
            for row in reader:
                data.append(row)
        
        top5 = [data.pop(random.randint(0, len(data) - 1)) for _ in range(random.randint(0, len(data)*3//10))]
        top15 = [data.pop(random.randint(0, len(data) - 1)) for _ in range(random.randint(len(data)*3//10, len(data)//2))]
        top20 = [data.pop(random.randint(0, len(data) - 1)) for _ in range(random.randint(len(data)*3//10, len(data)//2))]
        bottom5 = [data.pop(random.randint(0, len(data) - 1)) for _ in range(random.randint(0, len(data)*3//10))]
        if data:
            top20.extend(data)

        for student in top5:
            student.extend([random.randint(80, 100) for _ in range(10)])
        for student in top15:
            student.extend([random.randint(75, 90) for _ in range(10)])
        for student in top20:
            student.extend([random.randint(60, 85) for _ in range(10)])
        for student in bottom5:
            student.extend([random.randint(50, 75) for _ in range(10)])
        
        new_data = top5 + top15 + top20 + bottom5
        new_data.sort(key=lambda x: x[0])

        os.makedirs(os.path.join(parent_dir, f"semester {i}"), exist_ok=True)

        score_file = open(os.path.join(parent_dir, f"semester {i}", f"{csv_file[:-4]} Score.csv"), 'w', newline='')
        score_writer = csv.writer(score_file)
        score_writer.writerows(header + new_data)
        score_file.close()
