nums=list(map(int,input().split()))

def maxSubArray(nums) -> int:
    maxsum=max(nums)
    currsum=0
    for i in range(len(nums)):
        currsum+=nums[i]

        maxsum=max(currsum,maxsum)
        # print(currsum)
        if currsum<0:
            currsum=0
    return maxsum

print(maxSubArray(nums))