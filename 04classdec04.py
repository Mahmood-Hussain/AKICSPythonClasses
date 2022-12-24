"""
if (condition/statement):
    statements (body)
elif (condition/statement):
    statements (body)
else:
    statements (body)

"""

tesla_price = 7000000
iphone_price = 100000
usa_qual_research_papers = 4


mahmood_balance = 10000000
kumail_balance = 50000
muslims_published_papers = 4

if (mahmood_balance > tesla_price):
    print('Mahmood can buy a Tesla!')

if (kumail_balance > iphone_price):
    print('Kumail can buy an iPhone')
else:
    print('Kumail has insufficient balance so he can not buy an iPhone')

if (muslims_published_papers >= usa_qual_research_papers):
    print('Muslim is eligible to apply for USA universities')



# Grade System
"""
90-100 -> A+
80-90 -> A
70-80 -> B+
60-70 -> B
50-60 -> C
33-50 -> D
below 33 -> Fail
"""
student_marks = [87, 60, 66, 44, 32, 99, 94, 87, 93, 71, 65, 54, 55, 98, 90]
#print sequence: A , B,  B,  D,  F,  A+, A+, A,  A+, B+, B,  C,  C,  A+, A+
n_students = len(student_marks)
print(f'Number of Students: {n_students}') #fstring
i = 0
students_with_a_plus = 0
students_with_c = 0

while(n_students >= 1):

    current_student_marks = student_marks[i]
    if (current_student_marks >= 90):
        print('A+')
        students_with_a_plus = students_with_a_plus + 1
    elif (current_student_marks >= 80 and current_student_marks < 90):
        print('A')
    elif (current_student_marks >= 70 and current_student_marks < 80):
        print('B+')
    elif (current_student_marks >= 60 and current_student_marks < 70):
        print('B')
    elif (current_student_marks >= 50 and current_student_marks < 60):
        print('C')
        students_with_c = students_with_c + 1
    elif (current_student_marks >= 33 and current_student_marks < 50):
        print('D')
    else:
        print('Fail')

    n_students = n_students - 1
    i = i + 1

print(f'Students with A+ grade are: {students_with_a_plus}')

