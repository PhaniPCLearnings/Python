student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_Grade={}

for key in student_scores.keys():
    if student_scores[key]>=91 and student_scores[key]<100:
        student_Grade[key]="Outstanding"
    elif student_scores[key]>=81 and student_scores[key]<90:
        student_Grade[key]='Exceeds Expectations'
    elif student_scores[key]>=71 and student_scores[key]<80:
        student_Grade[key]='Acceptable'
    else:
        student_Grade['key']='Fail'

print(student_scores)
print(student_Grade)