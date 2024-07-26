from itertools import combinations

arr=list(map(int,input().split()))

arr1=combinations(arr,2)

for i in arr1:
    print(i)