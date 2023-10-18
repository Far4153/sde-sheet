n=int(input())
start=list(map(int,input().split()))
end=list(map(int,input().split()))
def maximumMeetings(n,start,end):
    arr=[]
    for i in range(n):
        arr.append([end[i],start[i],i])
    arr.sort()

    count=1
    limit=arr[0][0]
    for i in range(1,n):
        if arr[i][1]>limit:
            count+=1
            limit=arr[i][0]
        else:
            continue
    return count
    
print(maximumMeetings(n,start,end))




       

        


