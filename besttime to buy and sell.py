prices=list(map(int,input().split()))


def max_profit(prices):
    maxsum=0
    i=0
    j=1
    while(j<len(prices)):
            # print(currsum)
        if prices[i]<prices[j]:
            currsum=prices[j]-prices[i]
            maxsum=max(currsum,maxsum)
                
        else:
            i=j
        j+=1
    return maxsum


print(max_profit(prices))
        



