#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations
#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    result_arr = [-1]
    max_com = 0
    com_sticks = list(combinations(sticks, 3))
    for item in com_sticks :
        sort_item = sorted(item)
        if sort_item[2] < sort_item[1] + sort_item[0]:
            if sum(sort_item) > max_com :
                max_com = sum(sort_item)
                result_arr = sort_item
        
    # Return value must be array type
    return result_arr
            
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
