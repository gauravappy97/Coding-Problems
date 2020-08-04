#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(n, k, arr):
    arr = set(arr)
    ans = 0
    for i in arr:
        if (i+k in arr):
            ans+=1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
