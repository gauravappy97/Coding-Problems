#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    mylist = []
    for i in (s):
        mylist+=i
    resultlist = [[2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6],[4, 9, 2, 3, 5, 7, 8, 1, 6],[6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 1, 6, 3,     5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    a = []
    for i in resultlist:
        a.append(sum([abs(mylist[j]-i[j]) for j in range(0,9)]))
    return min(a)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
