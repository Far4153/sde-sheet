A=(3,1,2,5,3)
def repeatedNumber( A):
    n=len(A)
    new=[0]*n
    for i in range(n):
        new[A[i]-1]+=1
    print(new)

    for i in range(n):
        if new[i]==2:
            a=i+1
        if new[i]==0:
            b=i+1

    return a,b

print(repeatedNumber(A))

# timecomplexity: O(2n)
# space complexity= O(n) instead of O(1)
    

