# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, curr = 0, head
        while curr:
            n, curr = n + 1, curr.next
        m, r = divmod(n, k)
        if m == 0:
            r -= k

        res, curr, j = [None] * k, head, 0
        while curr:
            res[j] = curr
            j += 1
            for i in range(1, m):
                curr = curr.next
            if r > 0:
                r, curr = r - 1, curr.next
            tmp, curr.next = curr.next, None
            curr = tmp

        return res
