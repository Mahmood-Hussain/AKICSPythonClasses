# Array/List Methods/Operations (https://docs.python.org/3/tutorial/datastructures.html)
# Functions

observations = [2, 7, 3, 12, 9]
male_heights = [5.9, 5.8, 6.1, 6.2, 5.7, 6.4]
female_heights = [5.4, 5.3, 6.4, 5.1, 5.7, 4.9]
mixed_list = [4.6, 66, 'kangir', 'pheran'] # normally not much useful

# 10 observations of internal resitance of PCB
# [3.20, 3.22, 3.22, 3.19 ,  ... ] you keep adding those readings to the list -> append

"""
your_list.append(some_new_element) -> it adds/appends the element provided as 
argument to the end of the list
your_list is the variable name to some list of items (python list)

your_list.pop() -> removes the last element from the list

your_list.pop(some_element_index) -> removes an element from the list at given index



your_list.remove(some_element) -> remove some element from the list but if there are more than one
matches it will remove the first one from left to right

your_list.count('some_element') -> returns number about how many times some_element 
appeares in the list

"""

male_heights = [5.9, 5.8, 6.1, 6.2, 5.7, 6.4]
print(f'Orignal Male Heights Array: {male_heights}')
new_m_std_height = 6.1
# Now we want to add this new student height to our male_heights list at the end
male_heights.append(new_m_std_height)
print(f'Newly Appended: {male_heights}')


female_heights = [5.4, 5.3, 6.4, 5.1, 5.7, 4.9]
print(f'Orignal Female Heights Array: {female_heights}')
desired_idx = len(female_heights) - 1
female_heights.pop(desired_idx)

print(f'Modified Female Heights Array: {female_heights}')


# students = [
#     'mahmood', 'hussain', 'ahsan', 'jamsheed', 'kumail', 'muzafar', 'shahid', 
#     'muslim', 'willayat', 'illayat', 'sajaad', 'anayat', 'qasim', 
#     'hamza', 'umar', 'ali', 'qasim'
# ]
# students_marks = [
#     88, 90, 98, 60, 80, 90, 72, 
#     78, 66, 78, 98, 65, 99, 
#     87, 55, 50, 99
# ]

# your_list.remove(some_element)

kashmiri_items = ['kangir', 'pheran', 'khraaw', 'chalan', 
                    'kuang', 'harisa']

print(f'1: kashmir items {kashmiri_items}')

#####################################
new_item_1 = 'kangir'
numer_of_times = kashmiri_items.count(new_item_1)
if (numer_of_times > 0):
    print(f'{new_item_1} already exists in the list')
else: 
    kashmiri_items.append(new_item_1)
#####################################

print(f'2: kashmir items {kashmiri_items}')

#####################################
new_item_2 = 'wazwaan'
numer_of_times = kashmiri_items.count(new_item_2)
if (numer_of_times > 0):
    print(f'{new_item_2} already exists in the list')
else:
    kashmiri_items.append(new_item_2)
#####################################

print(f'3: kashmir items {kashmiri_items}')

#####################################
new_item_3 = 'allhach'
numer_of_times = kashmiri_items.count(new_item_3)
if (numer_of_times > 0):
    print(f'{new_item_3} already exists in the list')
else:
    kashmiri_items.append(new_item_3)
#####################################

print(f'4: kashmir items {kashmiri_items}')