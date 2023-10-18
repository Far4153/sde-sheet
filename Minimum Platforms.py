n=int(input())
arr=list(map(int,input().split()))
dep=list(map(int,input().split()))
def maximumMeetings(n,arr,dep):
    all=[]
    for i in range(n):
        all.append([dep[i],arr[i],i])
    all.sort()
    print(all)
    count=1
    limit=all[0][0]
    for i in range(1,n):
        print(all[i][1],limit)
        if all[i][1]<limit:
            count+=1
            print(count)
            limit=all[i][0]
        else:
            limit=all[i][0]
    return count
    
print(maximumMeetings(n,arr,dep))




       

        


