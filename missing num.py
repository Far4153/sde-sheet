nums=list(map(int,input().split()))


for i in range(0,len(nums)):
    if i not in nums:
        print(i)