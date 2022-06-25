# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 6/24/2022
# Description: Write a function that takes an integer list and returns the list with its
#              elements rotated to the right. A list is said to be rotated if all
#              elements of the array are moved to its right by one position.

# Solution # 1:

def rotate_right(num_list):

    if len(num_list) == 0 or len(num_list) == 1:
        return num_list

    else:
        last_num = num_list.pop()
        num_list.insert(0, last_num)
        return num_list

print(rotate_right([1, 2, 3, 4, 5]))

# Solution # 2:

def rotate_right_2(num_list):

    if len(num_list) == 0 or len(num_list) == 1:
        return num_list

    rotated_nums_list = [num_list[-1]]

    for num in num_list:
        if num != num_list[-1]:
            rotated_nums_list.append(num)
    return rotated_nums_list

print(rotate_right_2([]))

# Solution # 3:

def rotate_right_3(num_list):

    if len(num_list) == 0 or len(num_list) == 1:
        return num_list

    for index in range(len(num_list)):

        if index == 0:
            temp = num_list[index]
            num_list[index] = num_list[index - 1]

        elif index == 1:
            new_temp = num_list[index]
            num_list[index] = temp

        else:

            if temp not in num_list:
                new_temp = num_list[index]
                num_list[index] = temp

            else:
                temp = num_list[index]
                num_list[index] = new_temp

    return num_list

print(rotate_right_3([6, 7, 8, 9, 10]))