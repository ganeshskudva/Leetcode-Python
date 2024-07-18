# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.tmp = head

        def check(head):
            if not head:
                return True

            isPal = False
            if check(head.next) and self.tmp.val == head.val:
                isPal = True
            self.tmp = self.tmp.next

            return isPal

        return check(head)
