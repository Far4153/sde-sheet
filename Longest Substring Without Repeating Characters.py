s= input()
hashset=set()
l=0

maxx=0
for r in range(len(s)):
    print(l,r)
    while s[r] in hashset:
        hashset.remove(s[l])
        l+=1
    hashset.add(s[r])
    maxx=max(maxx,r-l+1)

print(maxx)