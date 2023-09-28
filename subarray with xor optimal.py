A=list(map(int,input().split()))
target=int(input())

dict1={}
xor=0
cnt=0

for i in range (len(A)):
    xor^=A[i]

    if xor==target:
        cnt+=1

    else:
        if xor not in dict1:

            dict1[A[i]]=i
            

      



