#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    answer = []
    for i in grades :
        if i < 38 :
            answer.append(i)
        else :
            if i % 3 <= 2:
                if i % 5 <= 2 :
                    answer.append(i)
                else :
                    for cnt in range(0,3):
                        if (i+cnt) % 5 == 0 :
                            answer.append(i+cnt)
                            break
            else :
                 answer.append(i)
                
    return answer
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
