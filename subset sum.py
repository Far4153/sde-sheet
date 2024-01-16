class Solution:
	def subsetSums(self, arr, N):
		# code here
		ans=[]
		
		def subset(ind, sum):
		    
		    if ind==N:
		        ans.append(sum)
		        return
		    
		        
		    subset(ind+1,sum+arr[ind])
		    subset(ind+1,sum)
		    
		subset(0,0)
		
		ans.sort()
		return ans