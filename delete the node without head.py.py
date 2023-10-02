class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextnode=node.next
        node.val=nextnode.val
        # print(nextnode)
        node.next=nextnode.next
