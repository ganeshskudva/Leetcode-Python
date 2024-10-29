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
        # Edge case: if the input list is empty, return None
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        mp, node = {}, head

        # First pass: create a copy of each node and store it in the map
        # Time Complexity (TC): O(N) as we traverse all nodes once
        # Space Complexity (SC): O(N) for storing copies of nodes in the dictionary `mp`
        while node:
            mp[node] = Node(node.val)  # Copy node with the same value
            node = node.next

        # Reset node to head to start second pass
        node = head

        # Second pass: set next and random pointers for the copied nodes
        # Time Complexity (TC): O(N) as we traverse all nodes once again
        # Space Complexity (SC): O(N) for using the same dictionary `mp` to set pointers
        while node:
            if node.next in mp:
                mp[node].next = mp[node.next]  # Link next pointer of copied node
            if node.random in mp:
                mp[node].random = mp[node.random]  # Link random pointer of copied node
            node = node.next

        # Return the head of the copied list
        return mp[head]

# Overall Time Complexity (TC): O(N) due to the two linear passes over the list
# Overall Space Complexity (SC): O(N) due to the dictionary `mp` storing each node copy

