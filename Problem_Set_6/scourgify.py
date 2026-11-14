import csv
import sys
#students.csv
#students_sorted.csv

if len(sys.argv) > 3:
    print("Too many arguments given")
    sys.exit()
try: 
    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})
#students: List <student>
#student: {name: str, house: str}

    for student in students:
        name_list = student['name'].split(", ")

        last_name = name_list[0]
        first_name = name_list[1]
        house = student['house']
        
        with open(sys.argv[2], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
            writer.writerow({"first name": first_name, "last name": last_name, "house": house})
except FileNotFoundError:
    print("File does not exist")
except IndexError:
    print("File name not given")