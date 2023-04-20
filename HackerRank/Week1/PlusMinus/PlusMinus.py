#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus, minus, zero = 0, 0, 0

    for i in arr :
        if i < 0 :
            minus += 1
        elif i == 0 :
            zero += 1
        else :
            plus += 1

    print(format(plus/len(arr),'.6f'))
    print(format(minus/len(arr),'.6f'))
    print(format(zero/len(arr),'.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
