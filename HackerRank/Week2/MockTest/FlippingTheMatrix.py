#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    sum = 0
    lm = len(matrix)
    quad = lm//2
    for i in range(quad):
        for j in range(quad):
            p1 = matrix[i][j]
            p2 = matrix[i][lm-j-1]
            p3 = matrix[lm-i-1][j]
            p4 = matrix[lm-i-1][lm-j-1]
            sum += max(p1, p2, p3, p4)
    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
