import unittest
from classes.student import Student

# This class is to test the Student class

class StudentTest(unittest.TestCase):

    # Instantiating an object with a type Student
    student = Student("Mark")

    # Testing the constructor of the class
    def test_0_constructor(self):
        print("Start constructor test\n")
        # Creating a new student with valid data and asserting the values
        student = Student("Mark", 50, 30, 20)
        self.assertEqual(student.blackboard, 50)
        self.assertEqual(student.lab, 30)
        self.assertEqual(student.written, 20)

        # Creating a new student with invalid blackboard points and asserting that it was set to 0
        student = Student("Andrew", 60, 10, 25)
        self.assertEqual(student.blackboard, 0)
        self.assertEqual(student.lab, 10)
        self.assertEqual(student.written, 25)

    # Testing the get points sum function
    def test_1_get_points_sum(self):
        print("Start get_points_sum test\n")
        # Giving some values and asserting that the sum is calculated properly
        self.student.blackboard = 50
        self.student.lab = 50
        self.student.written = 50
        self.assertEqual(self.student.get_points_sum(), 150)

        # Giving some values and asserting that the sum is calculated properly
        self.student.blackboard = 10
        self.student.lab = 30
        self.student.written = 20
        self.assertEqual(self.student.get_points_sum(), 60)

        # Giving new values and asserting that the sum is calculated properly
        self.student.blackboard = 10
        self.student.lab = 10
        self.student.written = 10
        self.assertEqual(self.student.get_points_sum(), 30)

    # Testing the get grade function
    def test_2_get_grade(self):
        print("Start get_grade test\n")
        # Giving random grades and checking if the grade is calculated properly (Very good)
        self.student.blackboard = 50
        self.student.lab = 50
        self.student.written = 50
        self.assertEqual(self.student.get_grade(), "Very good")

        # Giving new grades and checking if the grade is calculated properly (Failed)
        self.student.blackboard = 10
        self.student.lab = 30
        self.student.written = 20
        self.assertEqual(self.student.get_grade(), "Failed")

        # Giving random grades and checking if the grade is calculated properly (Satisfactory)
        self.student.blackboard = 50
        self.student.lab = 20
        self.student.written = 10
        self.assertEqual(self.student.get_grade(), "Satisfactory")

        # Giving random grades and checking if the grade is calculated properly (Good)
        self.student.blackboard = 40
        self.student.lab = 50
        self.student.written = 30
        self.assertEqual(self.student.get_grade(), "Good")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
