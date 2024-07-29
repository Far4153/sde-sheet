x=int(input())
if x < 0:
    neg=1
x=str(abs(x))
rev_str=x[::-1]
if int(rev_str)>(2**31-1):
    print(0)
elif neg==1:
    print(-(int(rev_str)))


