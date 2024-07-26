import numpy as num
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if num.sqrt(i) % 1 == 0:
        c+=1

print(c)