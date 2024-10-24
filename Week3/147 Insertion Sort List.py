# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        it = head
        low = 999999
        solver = None 
        while it != None:
            if it.data < low:
                solver
            it = it.next
        # more code to go through a linked list