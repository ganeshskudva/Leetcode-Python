class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.head = ListNode(-1)
        res = self.head

        def solve(n1, n2, carry=0):
            if not n1 and not n2 and not carry:
                return
            tot = carry
            if n1:
                tot += n1.val
            if n2:
                tot += n2.val
            self.head.next = ListNode(tot % 10)
            self.head = self.head.next
            carry = tot // 10
            solve(n1.next if n1 else None, n2.next if n2 else None, carry)

        solve(l1, l2)
        return res.next
