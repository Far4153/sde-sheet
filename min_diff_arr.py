
arr=list(map(int,input().split()))

arr.sort()
min_diff=arr[1]-arr[0]
for i in range(1,len(arr)):
    if min_diff>(arr[i]-arr[i-1]):
        min_diff=(arr[i]-arr[i-1])


sol_arr=[]

for i in arr:
    if (i+min_diff) in arr:
        sol_arr.append([i,i+min_diff])
print(sol_arr)