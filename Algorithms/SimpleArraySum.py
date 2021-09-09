#!/bin/python3

import math
import os
import random
import re
import sys

# Autor: Ricardo Conchas
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar_count, ar):
    while(ar_count < 9):
        print(ar_count)
        ar_count +=1
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
