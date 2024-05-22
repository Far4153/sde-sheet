arr=list(map(int, input().split(" ")))
arr.sort()
count=1
print(arr)
newpair=0
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        print(count)
        count+=1
    else:
        pair=count//2
        count=0
        newpair+=pair 
print(newpair)
