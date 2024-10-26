# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize the sorted portion of the list to be the first node
        sorted_head = ListNode(0)
        sorted_head.next = head
        sorted_tail = head
        
        # Start with the second node in the list, since the first node is already sorted
        curr = head.next
        solver = None
        it = head
        low = 999999 #look up max later
        
        lllength = 0 
        while it != None:
            lllength += 1
            if it.val < low:
                #solver.append( it.val)
                low = it.val
                # finds the lowers

                #next find the lowest that's biggere than low
            it = it.next
        sorted_head = ListNode(low)
        new_low = 999999 

        solver = sorted_head
        
        for i in range(lllength):
            this_node = head

            while this_node != None:
                if this_node.val < new_low and this_node.val > low:
                    low = this_node.val
                this_node = this_node.next

            solver.next = ListNode(new_low)
            solver = solver.next

        return sorted_head
        #while 
        # more code to go through a linked list



    #######

    test_ll = ListNode(5, ListNode(6, ListNode(4, ListNode(7, ListNode(2, ListNode(3, ListNode(1, ListNode(8))))))))

    print (insertionSortList( test_ll))

