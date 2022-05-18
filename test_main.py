from unittest import mock
from main import main
from main.main import students

# This file is to test the main.py script which has the main functions

# Testing the adding student function


def test_add_student():
    # Assigning the initial length to a variable
    num_students = len(students)

    # Simulating user input with some random data for a new student
    with mock.patch('builtins.input', side_effect=['New Student', 20, 50, 50]):
        # Creating a variable with the newly created student
        newStudent = main.addStudent()
        # Assertions on the new students that it was created with the given values
        assert newStudent.name == 'New Student'
        assert newStudent.blackboard == 20
        assert newStudent.lab == 50
        assert newStudent.written == 50

        # Asserting that the student was added successfully to the students list
        assert len(students) == num_students + 1


# Testing the deleting student function
def test_delete_student():
    # Assigning the initial length to a variable
    num_students = len(students)
    print(num_students)
    # Simulating the user input with id 1 so we delete student number 1
    with mock.patch('builtins.input', side_effect=[1]):
        # Calling the delete function
        main.deleteStudent()
        # Making sure that the list was reduced by one student
        assert len(students) == num_students - 1
        num_students -=1
        
    # Simulating the user input with invalid id then with the correct one
    with mock.patch('builtins.input', side_effect=[-2, 1]):
        # Calling the delete function
        main.deleteStudent()
        # Making sure that the list was reduced by one student
        assert len(students) == num_students - 1
        num_students -=1

# Testing that the display_students function that it doesn't cause any errors as it has no return value
def test_display_students():
    main.displayStudents(students)


# Testing the controller function
def test_controller():
    # Assigning the initial length to a variable
    num_students = len(students)

    # Choosing option 3 which is deleting a student and giving id 1
    with mock.patch('builtins.input', side_effect=[3, 1]):
        main.controller()
        # Asserting that the student with id 1 was deleted
        assert len(students) == num_students-1
        num_students -=1
        
    # Choosing option 2 which is adding a student and giving random data
    with mock.patch('builtins.input', side_effect=[2, 'New Student', 20, 50, 50]):
        main.controller()
        # Asserting that a new student was added
        assert len(students) == num_students+1
        num_students +=1
        
    # Choosing option 1 which is displaying all students
    with mock.patch('builtins.input', side_effect=[1]):
        main.controller()
