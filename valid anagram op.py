s=input()
t=input()

#this takes up O(n) time complexity
# space is O(n) 
#for optimized valid anagram op.py
def Anagram(s,t):
    
    if len(s)!=len(t):
        return False
    countS={}
    countT={}
    
    for i in range (len(s)):
        countS[s[i]]= 1+countS.get(s[i],0)
        countT[t[i]]= 1+countT.get(t[i],0)
    for j in countS:
        if countS[j]!=countT.get(t[j], 0):
            return False 
    return True




    return True
print(Anagram(s,t))