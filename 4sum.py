nums=[2,2,2,2,2]
target=8
res=[]
nums.sort()
        # print(nums)
for  j in range(len(nums))  :
    if j>0 and nums[j]==nums[j-1]:
        continue

    for i in range(j+1,len(nums)):

        if i>j+1 and nums[i]==nums[i-1]:
            continue

        l,r=i+1,len(nums)-1

        while l<r:
            sum = nums[j]+nums[i]+nums[l]+nums[r]
            if sum < target:
                l+=1
            elif sum > target:
                r-=1
            else:
                res.append([nums[j],nums[i],nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
               
print(res)
