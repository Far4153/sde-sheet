nums=list(map(int,input().split()))
target=int(input())
lA=0
for i in range(len(nums)):
    xor=0
    for j in range(i,len(nums)):
        xor=xor^nums[j]
        # print(xor,nums[i])
        
        if xor==target:

            lA+=1
            # print("la:",lA)
        
print(lA)