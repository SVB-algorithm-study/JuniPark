#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_sc, min_sc = scores[0], scores[0]
    max_ans, min_ans = 0,0
    
    for sc in scores :
        if sc > max_sc :
            max_sc = sc
            max_ans +=1
        if sc < min_sc :
            min_sc = sc
            min_ans +=1       
    
    return max_ans, min_ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
