class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]

        def findcandidates(ind,target):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return
            
            if candidates[ind]<=target:
                ds.append(candidates[ind])#pick
                findcandidates(ind,target-candidates[ind])
                ds.pop() #non-pick
            findcandidates(ind+1,target)
        findcandidates(0,target)

        return ans