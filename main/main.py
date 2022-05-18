# Importing the student class
from classes.student import Student
# Importing the tabulate for making a students table
from tabulate import tabulate

# This file contains all the operations a user can do

# Creating a global list with all the students
students = []

# Creating & Adding random initial students to the list
s1 = Student("Zeyad", 35, 30, 40)
s2 = Student("Ahmed", 50, 30, 10)
s3 = Student("Laszlo", 10, 10, 10)
s4 = Student("Peter", 50, 50, 50)
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

# Function to add a new student to the list
def addStudent():
    # Getting the student name from the user
    studentName = input("Please enter the name of the student: ")

    while True:
        try:
            # Getting the blackboard points from the user
            blackboard = int(input(
                "Please enter the grade of the blackboard exercises in the range of 0- 50 points: "))
            # Asking the user again if the value is not in range
            if blackboard > 50 or blackboard < 0:
                print("Please enter a value from 0-50")
            else:
                # Storing the number to the variable if the value is valid
                break
        except:
            # Asking the user again if the value is not a number format
            print("That's not a valid number!")

    while True:
        try:
            # Getting the laboratory points from the user
            laboratory = int(input(
                "Please enter the grade of laboratory exercises in the range of 0- 50 points: "))
            # Asking the user again if the value is not in range
            if laboratory > 50 or laboratory < 0:
                print("Please enter a value from 0-50")
            else:
                # Storing the number to the variable if the value is valid
                break
        except:
            # Asking the user again if the value is not a number format
            print("That's not a valid number!")
    while True:
        try:
            # Getting the written points from the user
            written = int(input(
                "Please enter the grade from the written part in the range of 0- 50 points: "))
            # Asking the user again if the value is not in range
            if written > 50 or written < 0:
                print("Please enter a value from 0-50")
            else:
                # Storing the number to the variable if the value is valid
                break
        except:
            # Asking the user again if the value is not a number format
            print("That's not a valid number!")

    # Adding the new student to the student list
    students.append(Student(studentName, blackboard, laboratory, written))
    # Printing a message that the student was added successfully
    print("Student added successfully")
    # Returning the newly created student
    return Student(studentName, blackboard, laboratory, written)

# Function to display all the students in a table
def displayStudents(students):
    # Creating the headers for our table
    headers = ['ID', 'Name', 'Total points', 'Grade']
    # Creating the table variable
    table = []
    # Looping over the students list
    for i in range(len(students)):
        # Adding each student record to the table
        table.append(
            [i+1, students[i].name, students[i].get_points_sum(), students[i].get_grade()])

    # Printing the table using the Tabulate library
    print(tabulate(table, headers, tablefmt="pretty"),"\n")

# Function to delete a student by his ID shown in the students table
def deleteStudent():
    while True:
        try:
            # Getting the ID of the student to be deleted
            id = int(input(
                "Please enter the ID of the student: "))
            # Asking for the ID again if it's not in range
            if id > len(students) or id < 1 or not students:
                print("ID is not valid")
            else:
                # Deleting the student with the given ID
                del students[id-1]
                # Telling the user that the student was deleted successfully
                print("Student deleted successfully\n")
                break
        except:
            # Asking for the ID again if it's not valid
            print("That's not a ID!")

# Function to control the user operations
def controller():
    while True:
        try:
            # Asking the user to choose an operation to do
            choice = int(input(
                "Welcome to the Grading Systme, please choose from the following: \n1- Display all students\n2- Add new student\n3- Delete student\n"))
            # Asking for a choice again if it's not in range
            if choice > 3 or choice < 1:
                print("Please enter a valid choice")
            else:
                break
        except:
            # Asking for a choice again if it's not valid
            print("That's not a valid choice!")

    # Displaying the students table if the choice was 1
    if choice == 1:
        displayStudents(students)
    # Calling the addStudent function if the choice was 2
    elif choice == 2:
        addStudent()
     # Calling the deleteStudent function if the choice was 2
    elif choice == 3:
        deleteStudent()
