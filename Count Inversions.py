from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
    inversions=0
    start=0
    while start<n:
        for i in range(start+1,n):
            print(i,start)
            if(arr[i]<arr[start]):
                inversions+=1
        start+=1
    return inversions

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))