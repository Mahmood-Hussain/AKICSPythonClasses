import math

"""
[
    [1, 4, 6]
    [6, 9, 0]
    [44, 2, 0]
]
a(ij) => a(22) = 9
for <variable_name/iterator> in <list:generator>:
    # body 

# 'for' is a reserved keyword
# 'in' is a reserved keyword
"""
"""
range gives pointer (iterator) to the first element
of the sequence to be generated
range function -> generator
range(0, end, 1)
range(start, end, 1) # if only one argument is provided to range function
it treats that as 'end' and the start will be '0'
range(start, end, jump/step)

"""


# print(generator)



"""student_marks = [90, 33, 59, 60, 74, 55, 77, 49, 72, 10, 34]
            #   0 ,  1,  2,  3,  4,  5,  6,  7,  8
# len(student_marks) -> 5
n = 0
while(n <= len(student_marks) - 1):
    print(student_marks[n])
    n = n + 1 """
    
# n = 0, len(student_marks) 5, 0 <= 4: true, student_marks[0] -> 90, n = 1
# n = 1, len(student_marks) 5, 1 <= 4: true, student_marks[1] -> 33, n = 2
# n = 2, len(student_marks) 5, 2 <= 4: true, student_marks[2] -> 59, n = 3
# n = 3, len(student_marks) 5, 3 <= 4: true, student_marks[3] -> 60, n = 4
# n = 4, len(student_marks) 5, 4 <= 4: true, student_marks[4] -> 74, n = 5
# n = 5, len(student_marks) 5, 5 <= 4: true, student_marks[5] -> error X

"""student_marks = [90, 33, 59, 60, 74]
for element in student_marks:
    print(element)"""

# for i in range(0, 20): # end element is excluded
#     print(i)

"""for i in range(1, 101): # end element is excluded
    print(i)

for i in range(0, 100): # end element is excluded
    print(i+1)"""

# for i in range(100): # end element is excluded
#     print(i)

# for i in range(0, 100, 3): 
#     print(i)

for i in range(0, 100): 
    if i == 2:
        pass
    else:
        print(i)


# print(student_marks)

"""n = 10
nums = range(n)
for i in nums:
    print(i)"""

"""for i in range(10):
    print(i)"""

"""start = 50
end = 100
for i in range(start, end):
    print(i)"""

# Starting point is always included
"""
start = 88
end = 120
step = 4
for i in range(start, end, step):
    print(i, end=',')"""
    # 88, 92, 96, 100, 104, 108, 112, 116, ...

# len -> function
# it gives us the number of elements of a list
# student_marks = [90, 33, 59, 60, 74]
# print(len(student_marks))

# print(math.pow(2, 8))
# print(math.pi)
# print(math.sqrt(4))

# Q: print all even numbers between 0 - 20 using only for loop
"""
start = 0
end = 21
step = 2
for i in range(start, end, step):
    print(i)
"""

# Q: Print the table of 7 till 70

"""
start = 7
end = 71
step = 7
for i in range(start, end, step):
    print(i)
"""

# for i in range(20):
#     if (i % 2 == 0):
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

