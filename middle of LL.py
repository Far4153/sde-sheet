class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    curr=head
    cnt=0
    while curr:
        cnt+=1
    temp=head
    for i in range(cnt//2):
        temp=temp.next
    return temp

