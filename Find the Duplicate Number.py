nums=list(map(int,input().split()))
def findDuplicate(nums) :
    nums.sort()
    for i in range(1,len(nums)-1):
        if nums[i-1]==nums[i]:
            return nums[i-1]

print(findDuplicate(nums))
    





