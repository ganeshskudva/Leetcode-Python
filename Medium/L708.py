"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev, nxt = head, head.next
        inserted = False
        while True:
            if prev.val <= insertVal <= nxt.val or prev.val > nxt.val > insertVal or nxt.val < prev.val < insertVal:
                prev.next = Node(insertVal, nxt)
                inserted = True
                break

            prev, nxt = prev.next, nxt.next
            if prev == head:
                break

        if not inserted:
            prev.next = Node(insertVal, nxt)

        return head
