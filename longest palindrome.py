from collections import defaultdict
s=input()
str_count=defaultdict(int)
long_str=0
# odd_count=0
for i in s:
    str_count[i]+=1
    if str_count[i] % 2 == 0:
        long_str+=2


for j in str_count:
    if str_count[j] % 2:
        long_str+=1
        break
print(long_str)
