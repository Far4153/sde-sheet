# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        temp=head
        c=1
        while temp.next!=None:
            temp=temp.next
            c+=1
        temp.next=head
  
        k=k%c
        k=abs(c-k)
        
        
        for i in range(k):
            temp=temp.next
        head=temp.next
        temp.next=None
       
        return head
        

