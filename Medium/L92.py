class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        Reverse a portion of a linked list between positions m and n.
        
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # If the list is empty or m and n are the same, no need to reverse, so return the head as is.
        if not head or m == n: 
            return head
        
        # Create a dummy node to simplify edge cases (like reversing from the head).
        p = dummy = ListNode(None)  
        dummy.next = head  # Connect dummy node to the original head
        
        # Move `p` to the node just before the m-th node
        for i in range(m-1):
            p = p.next
        
        # `tail` will point to the m-th node, which will become the tail of the reversed portion
        tail = p.next

        # Reverse the sublist between m and n
        for i in range(n-m):
            # a) Store the next node after `p` in a temporary variable (the node to be reversed)
            tmp = p.next  
            
            # b) Move the node after `tail` to the position immediately after `p`
            p.next = tail.next  
            
            # c) Adjust the next pointer of `tail` to skip the moved node and link to the next one
            tail.next = tail.next.next  
            
            # d) Link the newly moved node (`p.next`) to the previous first node of the sublist (`tmp`)
            p.next.next = tmp  
        
        # Return the modified list, which starts at `dummy.next`
        return dummy.next
