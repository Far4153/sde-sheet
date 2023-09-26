nums=list(map(int,input().split()))

def majorityElement(nums):

    nums.sort()
    c=1
    res=nums[0]
    new=[]
    n=len(nums)
    print(nums)
    if n<=2:
        new.append(nums[0])
    for i in range(1,len(nums)):
        print(i)
        if nums[i]!=nums[i-1]:
            c=1
        else:
            c+=1
        print(c)
        if c>(n//3):
            res=nums[i]
            new.append(nums[i])
            # print(new)

        
    return new
    

majorityElement(nums)