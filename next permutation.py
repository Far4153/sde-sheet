nums=[]

def nextPermutation( nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    pivot=None
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            pivot=i-1

            break
    else:
        nums.reverse()

        return

    swap=len(nums)-1

    while nums[swap]<=nums[pivot]:
        swap-=1

    nums[pivot],nums[swap]=nums[swap],nums[pivot]

    nums[pivot+1:]=reversed(nums[pivot+1:])
        
    return

        









#bruteforce
# from itertools import permutations
 
# nums=[1,2,3]
# def nextpermutation(nums):
#     p = sorted(set(permutations(nums)))
#     for i in range(len(p)):
#         if list(p[i])==nums and i==len(p)-1:
#             return list(p[0])
#         if list(p[i])==nums and i<len(p)-1:
#             return list(p[i+1])
        

# def changenums(res):
#     i=0
#     while (res!=nums):
#         if res[i]!=nums[i]:
#             nums[i],nums[i+1]=nums[i+1],nums[i]

#     return nums

# res=nextpermutation(nums)
# changenums(res)
# print(nums)