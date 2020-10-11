#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getRoundResult' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER winning_suit
#  2. CHARACTER suit1
#  3. INTEGER number1
#  4. CHARACTER suit2
#  5. INTEGER number2
#

def getRoundResult(winning_suit, suit1, number1, suit2, number2):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    winning_suit = input()[0]

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        suit1 = first_multiple_input[0][0]

        number1 = int(first_multiple_input[1])

        suit2 = first_multiple_input[2][0]

        number2 = int(first_multiple_input[3])

        result = getRoundResult(winning_suit, suit1, number1, suit2, number2)

        fptr.write(result + '\n')

    fptr.close()
