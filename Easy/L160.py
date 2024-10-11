class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If either of the lists is empty, there can be no intersection
        if not headA or not headB:
            return None

        # Initialize two pointers, one for each list
        first, sec = headA, headB
        
        # Traverse both lists. If one pointer reaches the end of its list, it is switched to the head of the other list.
        # This guarantees both pointers will traverse the same number of steps.
        # If the lists intersect, they will eventually meet at the intersection point.
        # If not, both pointers will eventually become None (end of their respective lists).
        while first != sec:
            # Move pointer 'first' to the next node, or switch to the head of the other list if it reaches the end
            first = headB if not first else first.next
            
            # Move pointer 'sec' to the next node, or switch to the head of the other list if it reaches the end
            sec = headA if not sec else sec.next
        
        # Either they meet at the intersection node or at the end (None, meaning no intersection)
        return first

