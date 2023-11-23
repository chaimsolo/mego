class Grades:
    def __init__(self):
        self.sum_of_hebrew = 0
        self.sum_of_english = 0
        self.sum_of_math = 0

    def gettingGrades(self, i):
        print(f"Enyer grades for student {i}")
        self.three_grades = {
        "hebrew":  int(input("Enter the hebrew grade >>>")),
        "math":  int(input("Enter the math grade >>>")),
        "english": int(input("Enter the english grade >>>"))
        }



    def sum(self):

        self.sum_of_hebrew += self.three_grades["hebrew"]
        self.sum_of_english += self.three_grades["english"]
        self.sum_of_math += self.three_grades["math"]

    def average(self):
        self.av_of_hebrew = self.sum_of_hebrew
        self.av_of_english = self.sum_of_english
        self.av_of_math = self.sum_of_math
