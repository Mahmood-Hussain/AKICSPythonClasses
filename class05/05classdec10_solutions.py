"""numbers = 100
numbers = numbers - 1
numbers = numbers - 1
numbers = numbers - 1
print(numbers)

numbers = 100
numbers_1 = numbers - 1
numbers_2 = numbers_1 - 1
numbers_3 = numbers - 1
print(numbers)"""

n = 100
print((n*(n+1))/2)
sum_of_n_nat = 0
while (n >= 0):
    # Do some work
    sum_of_n_nat = sum_of_n_nat + n
    n = n - 1

print(sum_of_n_nat)

# Q2
n = 20
while (n >= 0):
    # do something
    if (n % 2 == 0):
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
    n = n - 1

# Q3
given_num = 4
flag = 0
i = 1
while (i <= given_num):
    # do something
    if (given_num % i == 0):
        flag = flag + 1
    # increment/add one to i
    i = i + 1

if (flag > 2):
    print(f'{given_num} is not a prime number')
else:
    print(f'{given_num} WOHOOOO!!! it is a prime number')

# it is sunny today
# Today is sunny
# Today, here is sunny