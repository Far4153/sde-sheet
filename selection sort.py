arr=list(map(int,input().split()))
for pos in range(len(arr)):
    cursmall=pos
            
    for j in range(pos+1, len(arr)):  #finding the lowest number in the arr
        if arr[cursmall]>arr[j]:
                cursmall=j
        # print(cursmall)
    
    arr[pos],arr[cursmall]=arr[cursmall],arr[pos] #swapping with the first element

for i in range(len(arr)):
    print(arr[i],end=" ")
    