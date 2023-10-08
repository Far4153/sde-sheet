# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1=''
        temp=head
        while temp!=None:
            # print(temp.val)
            str1+=str(temp.val)
            temp=temp.next
        print(str1)

        if str1[::-1]==str1:
            return True
        return False