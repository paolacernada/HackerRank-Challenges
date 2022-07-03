# Author: Paola Cernada
# GitHub username: paolacernada
# Date: 7/3/2022
# Description: Given a list of words followed by two words,
#              find the distance between the two words.
"""
Example:

Input:
S = ["the", "quick", "brown", "fox", "quick"]
word1 = "the"
word2 = "fox"
Output: 3
"""

def word_distance(word_list, word1, word2):

    if word1 == word2:
        return 0

    minimum_distance = len(word_list) + 1

    for index in range(len(word_list)):

        if word_list[index] == word1:
            for index2 in range(len(word_list)):

                if word_list[index2] == word2:
                    distance = abs(index - index2)

                    if distance < minimum_distance:
                        minimum_distance = distance

    return minimum_distance

print(word_distance(["the", "quick", "brown", "fox", "quick"], "the", "fox"))
