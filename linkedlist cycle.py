class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashdict={}
        temp=head
        while temp!=None:
            if temp.next not in hashdict:
                hashdict[temp.next]=temp.val
            else:
                return True
            temp=temp.next
        return False