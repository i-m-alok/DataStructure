#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    arr=[]
    opp={')', ']', '}'}
    top=-1
    s=s.strip()
    for x in s:
        if (len(arr)==0 or ((arr[-1] not in opp)and (x not in opp))):
            arr.append(x)
        elif(arr[-1] not in opp) and (x in opp):
            if(arr[-1]=='{' and x=='}'):
                arr.pop(-1)
            elif(arr[-1]=='[' and x==']'):
                arr.pop(-1)
            elif(arr[-1]=='(' and x==')'):
                arr.pop(-1)
            else:
                arr.append(x)
    #print(arr)
    if len(arr)==0:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
