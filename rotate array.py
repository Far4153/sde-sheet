nums=list(map(int,input().split()))
k=int(input())
k_nums=nums[len(nums)-k:]
nums=nums[:(len(nums)-k)]

nums=k_nums+nums
print(nums)