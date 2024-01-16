class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        N=len(nums)
        nums.sort()
        res=set()
        def subsets(ind, sub):
            if ind==N:
                sub.sort()
                res.add(tuple(sub))
                return
            subsets(ind+1,sub)
            sub.append(nums[ind])
            subsets(ind+1,sub)
            sub.pop()

        subsets(0,[])

        for it in res:
            ans.append(list(it))

        return ans