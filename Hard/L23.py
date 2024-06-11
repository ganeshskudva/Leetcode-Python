# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            
            l2.next = merge(l1, l2.next)
            return l2
        
        def partition(start, end):
            if start == end:
                return lists[start]
            
            if start >= end:
                return None
            
            q = (start + end) // 2
            l1, l2 = partition(start, q), partition(q + 1, end)
            
            return merge(l1, l2)
        
        return partition(0, len(lists) - 1)
