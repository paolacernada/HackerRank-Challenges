# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 6/24/2022
# Description: A palindrome is a sequence that reads the same backward as forward.
#              Write a function is_palindrome() that takes an integer list as a
#              parameter and outputs either True or False if it is a palindrome.

def is_palindrome(num_list):

    reversed_num_list = []
    for num in num_list:
        reversed_num_list.insert(0, num)

    if num_list == reversed_num_list:
        return True
    else:
        return False

print(is_palindrome([1, 2, 3, 2, 1]))
