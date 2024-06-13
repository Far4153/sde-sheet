i=int(input())
j=int(input())
k=int(input())
c=0
for a in range(i,j+1):
    rev_i=str(a)[::-1]
    print(abs((a-int(rev_i)))/k)
    if ((abs(a-int(rev_i)))/k)%1==0:
        c+=1
print(c)