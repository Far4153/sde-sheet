nums=list(map(int,input().split()))

la=0
for i in range(len(nums)):
    sum=0
    for j in range(i,len(nums)):
        sum+=nums[j]
        
        if sum==0:
            la=max(la,j-i+1)
        
print(la)