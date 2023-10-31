# works for only indian currency

coins=list(map(int,input().split()))
v=int(input())
r=v
min_c=0
coins.sort(reverse=True)
# print(coins)
for i in coins:
    # print(i)
    if r>=i:
        # print('in')
        NC=r//i
        r=r-(i*NC)
        min_c+=NC
        # print(NC,r,min_c)
        if r==0:
            break
if r!=0:
    print(-1)
elif r==0:
    print(min_c)






