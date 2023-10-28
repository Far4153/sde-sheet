# i have took this que as per the deadline if any
# of the other work has the same deadine then i would reject it.
# but the  real que is about work i.e., if 3 days is deadline 
# then other work which has 3 days deadline can be 
# completed befor 1 day thst is on 2nd day 


n=int(input())
Jobs=[]
for i in range(n):
    info=list(map(int,input().split()))
    Jobs.append(info)
Jobs.sort(key = lambda x: x[2],reverse=True)
print(Jobs)

maxi = Jobs[0][1]
for i in range(1, len(Jobs)):
    maxi = max(maxi, Jobs[i][1])



count=0
profit=0
# deadline=Jobs[0][1]
slot=[-1]*(maxi+1)


for i in range(n):
    for j in range(Jobs[i][1],0,-1):
        if slot[j]==-1:
            slot[j]=i
            count+=1
            profit+=Jobs[i][2]
            break
       
    

print(count,profit)
        




