#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    cnt = 0
    check_where = "up"
    for i in path :
        if i == "U":
            altitude +=1
        elif i == "D" :
            altitude -= 1
            
        if altitude < 0 and check_where == "up":
            check_where = "down"
            cnt +=1
        elif altitude >= 0: 
            check_where = "up"
            
    return cnt
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
