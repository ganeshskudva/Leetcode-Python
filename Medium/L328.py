class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or contains only one node, return it as is.
        if not head or not head.next:
            return head

        # Initialize three pointers:
        # 'odd' points to the first node, 'even' to the second, and 'evenHead' saves the head of the even list.
        odd, even, evenHead = head, head.next, head.next

        # Rearrange the list by alternating between odd and even nodes.
        while even and even.next:
            # Re-link odd node to the next odd node (skip the even node).
            odd.next = odd.next.next
            odd = odd.next  # Move 'odd' pointer to the next odd node.

            # Re-link even node to the next even node (skip the odd node).
            even.next = even.next.next
            even = even.next  # Move 'even' pointer to the next even node.

        # Connect the last odd node to the head of the even list.
        odd.next = evenHead

        # Return the reordered list starting from 'head'.
        return head
