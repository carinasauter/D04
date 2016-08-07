#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports

import math

# Body


def eval_loop():
    s = ''
    last_result = 'n/a'
    while s != "done":
        s = ''
        try:
            s = input("What do you want evaluated? ")
            if s == 'done':
                break
            last_result = eval(s)
            print(last_result)
        except:
            print("Sorry, I cannot evaluate this. If you are done, please say 'done'.")
    return last_result


###############################################################################
def main():
    eval_loop()

if __name__ == '__main__':
    main()
