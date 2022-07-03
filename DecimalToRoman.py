# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 7/3/2022
# Description: Given an integer n, convert the function
#              to the corresponding roman numbers.

def to_roman(num):

    roman_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                  ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
                  ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

    result = ""

    for roman_symbol, value in reversed(roman_list):

        if num // value:
            count = num // value
            result += (roman_symbol * count)
            num = num % value

    return result

print(to_roman(2500))