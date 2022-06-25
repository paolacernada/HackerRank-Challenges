# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 6/24/2022
# Description: Write a function that takes an integer list and an integer k.
#              The function should return the list with its elements rotated
#              to the right k number of times.

def rotate_right(num_list):

    if len(num_list) == 0 or len(num_list) == 1:
        return num_list

    else:
        last_num = num_list.pop()
        num_list.insert(0, last_num)
        return num_list

def rotate_elements(num_list, k):

    for _ in range(k):
        rotate_right(num_list)
    return num_list

print(rotate_elements([1, 2, 3, 4, 5], 3))

# Solution # 2:

def rotate_elements_2(num_list, k):

    for _ in range(k):

        if len(num_list) == 0 or len(num_list) == 1:
            return num_list

        else:
            last_num = num_list.pop()
            num_list.insert(0, last_num)

    return num_list

print(rotate_elements_2([1, 2, 3, 4, 5], 3))