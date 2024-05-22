arr=list(map(int,input().split()))

for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
        arr[i-1],arr[i]=arr[i],arr[i-1] #swapping with the adjacent high element to left

for i in range(len(arr)):
    print(arr[i],end=" ")