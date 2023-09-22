def majorityElement( nums) -> int:

    nums.sort()
    c=1
    res=nums[0]
    n=len(nums)
    # print(nums)
    for i in range(1,len(nums)):
            # print(i)
        if nums[i]!=nums[i-1]:
            if c>(n//2):
                    # print(n//2)
                res=nums[i-1]
                return res
            else:
                c=1
        else:
            c+=1
        res=nums[i-1]
        # print(c)
    return res