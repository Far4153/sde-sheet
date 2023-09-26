#boyers moore algo

nums=list(map(int,input().split()))

def majorityElement(nums):
    n=len(nums)
    c1,c2=0,0
    ele1,ele2=None,None

    for i in range(len(nums)):
        print(c1,c2,ele1,ele2)
        if c1==0 and ele2!=nums[i]:
            c1=1
            ele1=nums[i]
        elif c2==0 and ele1!=nums[i]:
            c2=1
            ele2=nums[i]
        elif nums[i]==ele1:
            c1+=1
        elif nums[i]==ele2:
            c2+=1
        else:
            c1-=1
            c2-=1
    new=[]
    c1,c2=0,0
    for i in nums:
        if i==ele1:
            c1+=1
        if i==ele2:
            c2+=1
    print(ele1, ele2 )
    if ele1==ele2 and c1>n//3:
        new.append(ele1)
    else:


        if c1>n//3:
            new.append(ele1)
        if c2>n//3:
            new.append(ele2)
    return new

print(majorityElement(nums))

