# Find mean, variance and standard deviation of [2, 7, 3, 12, 9] using for loop

# Given array
arr = [2, 7, 3, 12, 9]
# get the length of array (number of elements in array)
arr_len = len(arr)
# intialize variable arr_sum as 0 (0 is identity element to addition operation)
arr_sum = 0
# Looping through the array
for current_ele in arr:
    # adding current element to the array sum 
    # Notice: arr_sum + current_ele will be evaluated first because it's on
    # the right hand side of expression
    # Then arr_sum variable will be overriden with newly calcualted arr_sum + current_ele
    arr_sum = arr_sum + current_ele

# mean is sum of all observations / number of observations
mean = arr_sum / arr_len

variance_temp = 0
for current_ele in arr:
    variance_temp = variance_temp + ((current_ele - mean) ** 2)

# variance formula -> summation((current_element - mean) ^ 2) / n    
# in the above we calcuated only summation((current_element - mean) ^ 2) so 
# / n is missing from variance
variance = variance_temp / arr_len

# standard deviation formula -> square_root(variance)
standard_deviation = variance ** 0.5

print(mean, variance, standard_deviation)


##################################################################################################

# Find mean, variance and standard deviation of [2, 7, 3, 12, 9] using while loop

# Given array
arr = [2, 7, 3, 12, 9]
# get the length of array (number of elements in array)
arr_len = len(arr)
# intialize variable arr_sum as 0 (0 is identity element to addition operation)
arr_sum = 0
# initialize iterator to track which index we have traversed
iters = 0
# loop until iters becomes 4 and when it is 5 conditional inside loop is false and it wille come out of it
while (iters < arr_len):
    # create a variable current_ele and put arr[index] value inside it
    current_ele = arr[iters]
    # add current element to array sum
    arr_sum = arr_sum + current_ele
    # mark that we iterated one more element
    iters = iters + 1

mean = arr_sum / arr_len

variance_temp = 0
iters = 0
while (iters < arr_len):
    current_ele = arr[iters]
    variance_temp = variance_temp + ((current_ele - mean) ** 2) 
    iters = iters + 1

variance = variance_temp / arr_len
standard_deviation = variance ** 0.5

print(mean, variance, standard_deviation)

##################################################################################################

# Given n = 50000 find sum of first n natural numbers using for loop
n = 50000
n_nat_sum = 0
for i in range(n+1):
    n_nat_sum = n_nat_sum + i
print(n_nat_sum)


##################################################################################################

#  Given a target element target = 55 and an array 
#  marks = [33, 65, 90, 45, 55.5, 88, 90, 98, 75, 45, 55, 55.1, 55.4, 45.8, 88, 90, 76, 53] 
#  find if the target element is in the marks list using for loop

marks = [33, 65, 90, 45, 55.5, 88, 90, 98, 75, 45, 55, 55.1, 55.4, 45.8, 88, 90, 76, 53] 
target = 55
# So basically we can solve using two approaches 
# 1. iterating through each element of the array
# 2. By looping using range until the length of the array and accessing each element by its index
# USING FIRST APPROACH
for current_marks in marks:
    if current_ele == target:
        print('yes target is in the list of given marks')

# USING ANOTHER APPROACH
marks_len = len(marks)
for i in range(marks_len):
    if marks[i] == target:
        print('Target found using 2nd approach as well')


##################################################################################################

#  Given a target element target = 55 and an array 
#  marks = [33, 65, 90, 45, 55.5, 88, 90, 98, 75, 45, 55, 55.1, 55.4, 45.8, 88, 90, 76, 53] 
#  find if the target element is in the marks list using while loop
marks = [33, 65, 90, 45, 55.5, 88, 90, 98, 75, 45, 55, 55.1, 55.4, 45.8, 88, 90, 76, 53] 
target = 55
marks_len = len(marks)
i = 0
while (i < marks_len):
    if marks[i] == target:
        print('target found using while loop')
    i = i + 1

##################################################################################################
#  From the list of marks given in Q4 find
#  the number of students who have scored more than 70 marks
marks = [33, 65, 90, 45, 55.5, 88, 90, 98, 75, 45, 55, 55.1, 55.4, 45.8, 88, 90, 76, 53] 
target = 55
marks_len = len(marks)
i = 0
more_than_70 = 0
while (i < marks_len):
    if marks[i] > 70:
        more_than_70 = more_than_70 + 1
    i = i + 1
print(f'Students with more than 70 are: {more_than_70}')
