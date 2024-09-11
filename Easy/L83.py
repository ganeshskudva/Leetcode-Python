# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = head

        def solve(curr, prev=None):
            if not curr:
                return
            if prev:
                if curr.val == prev.val:
                    prev.next = curr.next
                else:
                    prev.next = curr
                    prev = prev.next
            else:
                prev = curr

            solve(curr.next, prev)

        solve(head)
        return res
