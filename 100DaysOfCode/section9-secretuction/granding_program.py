student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don"t change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

def classification(score):
    if score > 90:
        result = "Outstanding"
    elif score > 80:
        result = "Exceeds Expectations"
    elif score > 70:
        result = "Acceptable"
    else:
        result = "Fail"
    return result

for students in student_scores:
    score = student_scores[students]
    student_grades[students] = classification(score)

# 🚨 Don"t change the code below 👇
print(student_grades)