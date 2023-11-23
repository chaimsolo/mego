from grades_oop import Grades

grades = Grades()
list_of_grades = []

for i in range(5):
    list_of_grades.append(grades.gettingGrades(i + 1))
    grades.sum()
grades.average()
print(f"the average of hebrew is {grades.av_of_hebrew}")
print(f"the average of math is {grades.av_of_math}")
print(f"the average of english is {grades.av_of_english}")