class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        next_greater = self.removeNodes(node.next)

        node.next = next_greater
        if not next_greater or node.val >= next_greater.val:
            return node

        return next_greater
