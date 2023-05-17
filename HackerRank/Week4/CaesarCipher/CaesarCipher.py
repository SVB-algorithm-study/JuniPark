#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    answer = ''
    while k > 26 :
        k -= 26

    for i in s :
        # A-Z : 65-90 / a-z : 97-122
        if i.isalpha() :
            asc_num = ord(i) + k
            
            if i.isupper():
                if 65 <= asc_num <= 90:
                    answer += chr(asc_num)
                elif  90 < asc_num :
                    answer += chr(asc_num-26)
            else :
                if 97 <= asc_num <= 122:
                    answer += chr(asc_num)        
                elif  122 < asc_num :
                    answer += chr(asc_num-26)
        else :
            answer += i
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
