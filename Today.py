# Author: Paola Cernada
# GitHub username: paolacernada
# Date: //2022
# Description: ***

def rotate_right(num_list):

    for index in range(len(num_list)):
        temp = num_list[index]
        num_list[index] = num_list[index - 1]
        num_list[index - 1] = temp
    return num_list

print(rotate_right([1, 2, 3, 4, 5]))

