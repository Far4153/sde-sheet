intervals=[[1,3]]

intervals.sort()

res=[intervals[0]]
n=len(intervals)
# non_Ol=[]


for start, end in intervals[1:]:
    lastend=res[-1][1]
    print(lastend)
    if lastend>=start:
        res[-1][1]=max(end,res[-1][1])
    else:
        res.append([start,end])
        

print(res)