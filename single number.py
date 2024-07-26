nums=list(map(int,input().split()))
hashset=set()
for i in nums:
    if i in hashset:
        hashset.remove(i)
    else:
        hashset.add(i)
for i in hashset:
    print(i)