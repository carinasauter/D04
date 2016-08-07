#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


# Body

def letter_in_word(string, letter_searched):
    count = 0
    for letter in string:
        if letter == letter_searched:
            count += 1
    print(count)

###############################################################################


def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    letter_in_word('banana', 'a')
    letter_in_word('car', 'm')
    letter_in_word('this will be a really long string', 'l')


if __name__ == '__main__':
    main()
