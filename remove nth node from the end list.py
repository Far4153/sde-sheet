class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=ListNode()
        start.next=head
        fast=start
        slow=start

        for i in range(0,n):
            fast=fast.next
        
        while fast.next!=None:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        # print(head)
        # print(start)

        

        return start.next