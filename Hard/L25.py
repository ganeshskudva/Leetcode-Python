# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, cnt = head, 0
        while cnt < k:
            if not node:
                return head
            node = node.next
            cnt += 1
        
        prev = self.reverseKGroup(node, k)
        while cnt:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            cnt -= 1
        
        return prev
