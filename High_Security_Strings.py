#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING password
#  2. INTEGER weight_a
#

def getStrength(password, a):
    sum=0
    l=[i for i in range(a,26)]
    for i in range(a): l.append(i)
    for i in password: sum=sum+(l[ord(i)-97])
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = input()

    weight_a = int(input().strip())

    strength = getStrength(password, weight_a)

    fptr.write(str(strength) + '\n')

    fptr.close()
