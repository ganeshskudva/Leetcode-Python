class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the head is None, return None (end of the list)
        if not head:
            return head
        
        # Recursive case: move to the next node in the list
        node = head
        next_greater = self.removeNodes(node.next)
        
        # Set the current node's next pointer to the result of recursive call
        node.next = next_greater
        
        # If the next node is None or the current node's value is greater than or equal to the next node's value, return the current node
        if not next_greater or node.val >= next_greater.val:
            return node
        
        # Otherwise, skip the current node and return the next greater node
        return next_greater

# Time Complexity (TC): O(n), where n is the number of nodes in the linked list.
# The recursion goes through each node once, leading to linear time complexity.

# Space Complexity (SC): O(n), due to the recursive call stack. The maximum depth of recursion will be equal to the number of nodes in the list.
