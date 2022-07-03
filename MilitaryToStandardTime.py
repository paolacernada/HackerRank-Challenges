# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 7/3/2022
# Description: Write a function military_to_standard() that takes
#              two integer as parameters hours and minutes, that
#              returns the time converted from 24-hour format to
#              12-hour format.

def military_to_standard(hours, mins):

    if hours == 12 and mins == 0:
        return "12:00PM"

    if hours == 0 and mins == 0:
        return "12:00AM"

    elif hours > 12 and mins > 0:
        hours -= 12
        return f"{hours}:{mins}PM"

    else:
        return f"{hours}:{mins}AM"

print(military_to_standard(19, 30))
print(military_to_standard(6, 59))