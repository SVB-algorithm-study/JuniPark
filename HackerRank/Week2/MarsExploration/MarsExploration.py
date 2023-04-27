#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    cnt = 0
    for i in range(len(s)//3):
        message = s[i*3:i*3+3]
        if message != "SOS" :
            if message[0] != "S" :
                cnt +=1
            if message[1] != "O" :
                cnt +=1  
            if message[2] != "S" :
                cnt +=1         
                
    return cnt
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
