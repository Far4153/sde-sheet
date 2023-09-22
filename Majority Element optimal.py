def majorityElement( nums) -> int:
        
    c=0
    ele=None
    n=len(nums)
        # print(nums)
    for i in range(len(nums)):
        if c==0:
            c=1
            ele=nums[i]
        elif ele==nums[i]:
            c+=1
        else: 
            c-=1
        c=0
    for i in nums:
        if i == ele:
            c+=1
    if c>n//2:
        return ele

    return -1