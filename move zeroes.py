nums=list(map(int,input().split()))
c=0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[c]=nums[i]
        c+=1
    
for j in range(c,len(nums)):
    nums[j]=0
print(nums)