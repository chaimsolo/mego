from grades_oop import Grades


list_of_grades = []



for i in range(5):
    grades = Grades(i + 1)
    list_of_grades.append(grades(i + 1))
    print(f"The average score for student {i + 1} is ")
print(list_of_grades)



# for i in range(5)
# grades.average()
# print(f"the average of hebrew is {grades.av_of_hebrew}")
# print(f"the average of math is {grades.av_of_math}")
# print(f"the average of english is {grades.av_of_english}")