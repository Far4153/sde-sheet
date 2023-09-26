nums=list(map(int,input().split()))

#we use unordered set for storing elements
hashset=set()
n=len(nums)
c=0
longest=0

for i in nums:
    hashset.add(i)
# print(hashset)

for ele in range(n):
    # print(nums[ele])
    if nums[ele]-1 not in hashset:

        c=1
        x=ele

        while nums[x]+1 in hashset:
            nums[x]+=1
            c+=1 
            # print(c)

        longest=max(c,longest)
print(longest)