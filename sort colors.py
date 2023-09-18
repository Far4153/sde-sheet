nums=list(map(int,input().split()))

def sortColors( nums):
    i=0
    n=len(nums)
    
    for i in range(n):
        j=0
        while(j<n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            j+=1
        i+=1
    
    return nums

print(sortColors(nums))


