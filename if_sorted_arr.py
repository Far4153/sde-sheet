nums=list(map(int,input().split()))

sorted_nums=sorted(nums)

for i in range(len(nums)):
    c=nums[i]
    nums.pop(i)
    nums.append(c)
    print(nums)
    if sorted_nums==nums:
        print("True")
print("false")    