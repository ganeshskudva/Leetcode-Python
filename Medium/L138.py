"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp, node = {}, head
        while node:
            mp[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            if node.next in mp:
                mp[node].next = mp[node.next]
            if node.random in mp:
                mp[node].random = mp[node.random]
            node = node.next

        return mp[head]
