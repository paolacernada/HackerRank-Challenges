# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 6/24/2022
# Description: A function standard_to_military() that takes two parameters
#              hours and time_of_day, it then returns the hours and minutes
#              converted from 12-hour format to 24-hour format.

def standard_to_military(hours, time_of_day):

    if hours == 12 and time_of_day == "AM":
        return 0

    elif hours < 12 and time_of_day == "PM":
        hours += 12
        return hours

    else:
        return hours

print(standard_to_military(7, "PM"))
print(standard_to_military(1, "AM"))

