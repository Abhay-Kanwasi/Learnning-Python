# Given a dictionary with student names as keys and their scores as values, write a function to find the student with the highest score.

student = {}
for i in range(4):
    keys = input("Enter the student name : ")
    values = int(input("Enter the score of student : "))
    student[keys] = values

list = student.values()
maxium = []
for i in list:
    maxium.append(i)
print(max(list))

    
