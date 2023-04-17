#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    day = s[-2:]
    hour = int(s[:2])

    if day == "PM" and hour < 12:
        s = s.replace(s[:2],str(int(s[:2])+12))
    elif day == "AM" and hour == 12 :
        s = s.replace(s[:2],"00")

    return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
