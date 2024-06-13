
n=int(input())
k=int(input())
a=list(map(int, input().split(" ")))
threshold=0

for i in a:
    if i <= 0:
        threshold+=1
if threshold>=k:
    print("No")
else:
    print("Yes")
