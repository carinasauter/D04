# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

# Exercise 5
# A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed number of places.
# To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary,
# so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
# To rotate a word, rotate each letter by the same amount.
# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
# In the movie 2001: A Space Odyssey, the ship computer is called HAL,
# which is IBM rotated by -1.

# Write a function called rotate_word that takes a string and an integer as parameters,
# and returns a new string that contains the letters from the original
# string rotated by the given amount.

# You might want to use the built-in function ord, which converts a character to a numeric code,
# and chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical order,
# so for example:

# >>> ord('c') - ord('a')
# 2
# Because 'c' is the two-eth letter of the alphabet. But beware: the
# numeric codes for upper case letters are different.

# import

# body


def rotate_word(string, position_change):
    new_word = ''
    if abs(position_change) > 25:
        position_change = position_change % 26
    for letter in string:
        new_letternumber = ord(letter) + position_change
        if letter.islower():
            if new_letternumber > 122:
                new_letternumber = new_letternumber - 26
            elif new_letternumber < 97:
                new_letternumber = new_letternumber + 26
        else:
            if new_letternumber > 90:
                new_letternumber = new_letternumber - 26
            elif new_letternumber < 65:
                new_letternumber = new_letternumber + 26
        new_word = new_word + chr(new_letternumber)
    return new_word


def main():

    print(rotate_word('abc', 24))
    print(rotate_word('abc', 25))
    print(rotate_word('abc', -26))
    print(rotate_word('ABC', -30))
    print(rotate_word('XYZ', 45))

if __name__ == '__main__':
    main()
