"""
Colab Link for solutions of Assignmnt 4 - https://colab.research.google.com/drive/1QyVoHMnL05wC5LXLu7cH_izBVZofHU1F?usp=sharing
Python functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

syntax

def <function_name>(*arguments):
    body/statements


function_name(arg1, arg2, arg, ....) this does NOT RETURN value or INPLACE operation
result = function_name(arg1, arg2, arg, ....) this RETURNS a value (which is memory address to the result(s))

"""

def add_item(items, new_item):
    n = items.count(new_item)
    if (n > 0):
        print(f'{new_item} already exists in the list')
    else:
        items.append(new_item)


kashmiri_items = ['kangir', 'pheran', 'khraaw', 'chalan', 'kung', 'harisa']


new_item = 'wazwaan'
add_item(kashmiri_items, new_item)
print(kashmiri_items)

new_item = 'kangir'
add_item(kashmiri_items, new_item)
print(kashmiri_items)


def get_square(number):
    # return number * number
    # return number ** 2
    return pow(number, 2)


result = get_square(5)
print(result)

# kashmiri_items.reverse()
# print(kashmiri_items)


# you want me to skip all items at odd indices
n = len(kashmiri_items)
for i in range(0, n, 2):
    print(kashmiri_items[i])


