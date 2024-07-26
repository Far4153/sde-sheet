nums=list(map(int,input().split()))
c=0
maxsum=0
for i in nums:
    if i==1:
        c+=1
    else:
        c=0
    maxsum=max(c,maxsum)
print(maxsum)
