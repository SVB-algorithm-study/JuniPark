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
    # Write your code here
    # 대체 몇바퀴를 도는 거냐.....
    answer = 0
    lm = len(matrix)
    for i in range(lm) :
        for j in range(lm//2) :
            if matrix[i][j] < matrix[i][lm-1-j]:
                matrix[i][j], matrix[i][lm-1-j] = matrix[i][lm-1-j], matrix[i][j]
        
    for i in range(lm//2) :
        for j in range(lm) :
            if matrix[i][j] < matrix[lm-1-i][j]:
                matrix[i][j], matrix[lm-1-i][j] = matrix[lm-1-i][j], matrix[i][j]
            
            
    for i in range(len(matrix)//2) :
        for j in range(len(matrix[i])//2) :
            answer += matrix[i][j]
            # print(matrix[i][j])
            
    return answer

    # sum = 0
    # lm = len(matrix)
    # for i in range(lm//2):
    #     for j in range(lm//2):
    #         p1 = matrix[i][j]
    #         p2 = matrix[i][lm-1-j]
    #         p3 = matrix[lm-1-i][j]
    #         p4 = matrix[lm-1-i][lm-1-j]
    #         sum += max(p1, p2, p3, p4)
    # return sum
    

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
