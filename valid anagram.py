s=input()
t=input()

#this takes up O(nlogn + n) time complexity
# space is O(1) 
#for optimized valid anagram op.py
def Anagram(s,t):
    s=''.join(sorted(s))
    t=''.join(sorted(t))
    
    if len(s)!=len(t):
        return False
    for i in range (len(t)):
        if t[i] != s[i]:
            return False
    return True
print(Anagram(s,t))