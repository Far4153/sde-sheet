A=(3,1,2,5,3)
def repeatedNumber( A):
    n=len(A)
    S=0
    S2=0
    Sn=(n*(n+1))/2
    S2n=(n*(n+1)*((2*n)+1))/6
    
    for i in A:
        S+=i
        S2+=i*i
    EQ1=S-Sn
    EQ2=S2-S2n

    sumAB=EQ2/EQ1
    diffAB=EQ1

    a=(sumAB+diffAB)/2
    b=a-EQ1

    return a,b

print(repeatedNumber(A))