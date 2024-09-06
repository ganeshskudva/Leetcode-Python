# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, st = ListNode(-1, head), set(nums)
        curr, prev = head, dummy
        
        while curr:
            if curr.val in st:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        
        return dummy.next


#Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st = set(nums)

        def remove_nodes(curr):
            if not curr:
                return None
            curr.next = remove_nodes(curr.next)
            return curr.next if curr.val in st else curr

        return remove_nodes(head)
