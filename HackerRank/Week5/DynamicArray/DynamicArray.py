#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    ans = []
    
    for q in queries :
        q_type, x_num, y_num = q
        # print(q_type, x_num, y_num)
        
        # XOR operator : A ^ B
        idx = (x_num ^ lastAnswer) % n
        if q_type == 1 :
            arr[idx].append(y_num)
            
        elif q_type == 2 :
            lastAnswer = arr[idx][y_num % len(arr[idx])]
            ans.append(lastAnswer)
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
