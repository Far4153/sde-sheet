hashmap={}
target=10
nums=[2,4,6,9]
for i in range(len(nums)):
    
    if target-nums[i] not in hashmap:
        hashmap.update({nums[i]:i})
    else:
        print(hashmap[target-nums[i]],i)



