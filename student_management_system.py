from os.path import isdir
import random

class Students:
    student = []
    marks = []
    ids = []


c = Students()

# ---------------- ADD STUDENT ----------------

def add_student():
    count = 0
    user = 'o'
    with open("stud_records.txt", "a") as f:
        while user != 'n':
            name = input("Enter the name of student: ")
            while name.isdigit():
                name = input("Please enter a valid name of student: ")
            mark = input("Enter the marks of the student: ")

            user = input("Press y to add more students or n to stop: ")
            c.student.append(name)
            c.ids.append(random.randint(10000, 99999))
            c.marks.append(mark)
            f.write(c.student[count] + 5 * " " + c.marks[count] + 5 * " "
                    + str(c.ids[count]) + abs((80 - len(c.student[count]) - len(c.marks[count]) - len(
                str(c.ids[count])) - 10)) * " " + "\n")

            count += 1


# -------------------- REM STUDENT -----------------
def rem_student(find):
    counter = 0
    with open("stud_records.txt", "r+") as f:
        content = f.read()
        num = 0
        found = False
        for i in range(0, len(content)):
                if content[i:i+5] == find:
                        num = i
                        found = True
                        break

        if found:
            while 1:
                num-=1
                if content[num] == "\n":
                    break
            if num == -1:
                num+=1
            f.seek(num)
            f.write(80 * " " + "\n")
        else:
            print("No matching records")

#Show Students
def show_student():
    with open("stud_records.txt", "r+") as f:
        print(f.read())

def clear_records():
    with open("stud_records.txt", "w", newline="\n") as f:
        pass
# Updating student
def update_student(name,marks,id):
    counter = 0
    res = 0
    arr = []
    with open("stud_records.txt", "r+") as f:
        content = f.read()
        num = 0
        found = False
        for i in range(0, len(content)):
                if i<len(content)-4 and content[i].isdigit() and content[i+4].isdigit():
                    arr.append(content[i:i+5])
                else:
                    continue

        for i in range(len(arr)):
            if arr[i] == id:
                found = True
                break
            else:
                res+=81
        if found:
            f.seek(res+1)
            record = name + 5 * " " + marks + 5 * " "+ id
            record =  record.ljust(80)
            record += "\n"
            f.write(record)


check = int(input(
    "Enter 1 to add student\n"
    "2 to remove student\n"
    "3 to show students\n"
    "4 to update student\n"
    "5 to update student\n"
))
while check<0 or check>5:
    print("Please Enter between 1 to 5")
    check = int(input(
    "Enter 1 to add student\n"
    "2 to remove student\n"
    "3 to show students\n"
    "5 to clear records\n"))
if check == 1:
    add_student()

elif check == 2:
    find = input("Enter student id to remove: ")
    while len(find) != 5:
        find = input("Student id must be 5 digits: ")
    rem_student(find)

elif check == 3:
    show_student()

elif check == 4:
    id = input("Enter student id to update: ")
    while len(id) != 5:
        id = input("Student id must be 5 digits: ")

    name = input("Enter name of the student: ")
    marks = input("Enter the marks of the student: ")

    update_student(name, marks, id)

elif check == 5:
    clear_records()
