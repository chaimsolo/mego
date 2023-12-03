class Grades:
    def __init__(self):
        None

    def gettingGrades(self, i):
        print(f"Enter grades for student {i}")
        self.three_grades = {
            "hebrew": int(input("Enter the hebrew grade >>>")),
            "math": int(input("Enter the math grade >>>")),
            "english": int(input("Enter the english grade >>>"))
        }

    def average(self):
        return (self.three_grades["hebrew"] + self.three_grades["math"] + self.three_grades["english"]) / 3
