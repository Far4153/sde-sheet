n=int(input())
arr=list(map(int,input().split()))
dep=list(map(int,input().split()))
def maximumMeetings(n,arr,dep):        
    arr.sort()
    dep.sort()


    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        print(arr[i],dep[j],count)
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans

print(maximumMeetings(n,arr,dep))
