s=input()
singlecount=0
ss=set(s)
reslen=0
for i in ss:
    rescount=s.count(i)
    if  rescount>1 :
        reslen+=(rescount//2)*2
    else:
        singlecount=1
reslen+=singlecount
print(reslen)