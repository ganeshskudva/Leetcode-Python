class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        first, sec = headA, headB
        while first != sec:
            first = headB if not first else first.next
            sec = headA if not sec else sec.next
        
        return first
