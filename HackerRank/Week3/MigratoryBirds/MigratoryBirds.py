#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    num_dict = {}
    for i in arr :
        if i not in num_dict :
            num_dict[i] = 0
        num_dict[i] += 1
    
    key_arr = []
    for key, value in num_dict.items():
        if value == max(num_dict.values()) :
            key_arr.append(key)
    
    return min(key_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
