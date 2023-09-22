
def myPow(x: float, n: int) -> float:
    res=1
    nn=n
    if nn==0:
        return res
    while nn:
        if nn%2:
            res*=x
            nn=nn-1
        else:
            x=x*x
            nn=nn//2
    if n<0:
        res=1.0/res
    
    return res

print(myPow(0.876,2345678))