s=input()
seen=set()
long_str=0

for i in s:
    if i in seen:
        seen.remove(i)
        long_str+=2
    else:
        seen.add(i)

if seen:
    long_str+=1
print(long_str)