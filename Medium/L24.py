# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, k, cnt = head, 2, 0
        while cnt < k:
            if not node:
                return head
            
            node = node.next
            cnt += 1
        
        prev = self.swapPairs(node)
        while cnt > 0:
            nxt = head.next
            head.next = prev
            prev, head = head, nxt
            cnt -= 1
        
        return prev
