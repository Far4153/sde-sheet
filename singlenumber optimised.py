nums=list(map(int,input().split()))
res=0
for i in nums:
    res=res^i
print(res)