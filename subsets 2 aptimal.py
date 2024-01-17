class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        nums.sort()
        def subsets(ind):
            ans.append(ds[:])
            for i in range(ind,len(nums)):
                if i!=ind and  nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                subsets(i+1)

                # print(ds)
                ds.pop()
                # print(ds)

        subsets(0)
        return ans