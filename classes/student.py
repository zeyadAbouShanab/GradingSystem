# Student class

class Student:
    # Creating a range to be used in declaring the student's points
    valid_range = range(0, 51)

    # Class constructor
    def __init__(self, name="", blackboard=0, lab=0, written=0):
        # Assingning the values and if points value is not valid then it's set to 0
        self.name = name
        if blackboard in self.valid_range:
            self.blackboard = blackboard
        else:
            print("Blackboard grade not in range 0-50 and set to 0")
            self.blackboard = 0
        if lab in self.valid_range:
            self.lab = lab
        else:
            print("Lab grade not in range 0-50 and set to 0")
            self.lab = 0
        if written in self.valid_range:
            self.written = written
        else:
            print("Written grade not in range 0-50 and set to 0")
            self.written = 0           

    # Function to get the total points of the student
    def get_points_sum(self):
        return self.blackboard + self.lab + self.written

    # Function to grade the student depending on his sum of points
    def get_grade(self):
        if self.get_points_sum() in range(0,76):
            return "Failed"
        elif self.get_points_sum() in range(76,101):
            return "Satisfactory"
        elif self.get_points_sum() in range(101,126):
            return "Good"
        elif self.get_points_sum() in range(126,151):
            return "Very good"

