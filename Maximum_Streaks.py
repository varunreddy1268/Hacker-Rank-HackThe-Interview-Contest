#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(t):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    h,t1,k1,k2=[],[],0,0
    for i in range(len(t)):
        if t[i]=='Heads':
            k1=k1+1
            t1.append(k2)
            k2=0
        if t[i]=='Tails':
            k2=k2+1
            h.append(k1)
            k1=0
    t1.append(k2)
    h.append(k1)
    return (max(h),max(t1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
