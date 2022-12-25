# comparisions
# Conditional Operators / Logical Operators

"""
> 'greater than'
< 'less than'
>= 'greater or equal to'
<= 'less or equal to'
== 'equal to'
!= 'not equal to'

logical
AND -> and 'and'
OR -> or 'or'
NOT -> not 'not'

True
False
"""

print(33 > 12)
print(2 != 3)
print(99 == 99)

x = 2
y = 7
print(x >= y) # -> False

print(x <= y) # -> True

# Loops
arr = [2, 3, 4, 5, 8]
# print(arr[0])
# print(arr[4])
# print(arr[2])

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print(arr[5]) # IndexError: list index out of range

# while
# for loop

"""
while loop usage

while (statement or condition):
    statements

after every iteration the statement or a condition inside of the 
while parenthesis are checked again.

Until the conidtion or the statment evaluates to false
loop will keep on executing its body i.e statements inside of it

    
"""
"""

x = 5
print(x) #5
x = x - 1
print(x) #4
x = x - 1
print(x) #3
x = x - 2
print(x) #1
"""

x = 5
while (x >= 1):
    print(x)
    x = x - 1
print('this is control to main again')



arr = [2, 3, 4, 5, 8]
arr_len = len(arr) # len() function accepts array variable as arg and returns it's length i.e the number of elements
# 5
# print(arr_len)
i = 0
while (arr_len >= 1):
    print(arr[i])
    i = i + 1
    arr_len = arr_len - 1

# mid_index = arr_len // 2
# mid_ele = arr[mid_index]
# print(f'Middle Element is: {mid_ele}')

