#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """ This only checks if all letters are lower case. If not, then it returns false.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """ Will always return True.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Will only return True if the last letter in s is lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This one works :)
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Only works if all letters are lowercase. Otherwise the one false is going to set everything else to false
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():
    print(any_lowercase1("Hello"))
    print(any_lowercase2('HELLO'))
    print(any_lowercase3('HellO'))
    print(any_lowercase5('HeLLO'))


if __name__ == '__main__':
    main()
