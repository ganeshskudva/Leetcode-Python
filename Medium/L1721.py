class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Initialize two pointers n1 (for k-th node from start) and n2 (for k-th node from end).
        # p is used to traverse the list.
        n1, n2, p = None, None, head
        
        # Traverse the list to find the k-th node from the start (n1) and also set up n2 for the k-th node from the end.
        while p is not None:
            k -= 1
            # Start moving n2 once p has moved beyond the k-th node, so n2 ends up at the k-th node from the end.
            n2 = None if n2 == None else n2.next
            
            # When we reach the k-th node from the start, set n1 to that node, and n2 to head to begin moving it.
            if k == 0:
                n1 = p
                n2 = head
            
            # Move the pointer p to the next node in the list.
            p = p.next
        
        # Swap the values of the two nodes (n1 and n2) instead of swapping the actual nodes.
        # This is based on the problem statement's requirement to swap node values.
        n1.val, n2.val = n2.val, n1.val
        
        # Return the head of the modified list.
        return head

# Time Complexity (TC):
# 1. The loop runs exactly once over the entire linked list, so the traversal takes O(n), where n is the number of nodes in the list.
# 2. The value swapping takes constant time, O(1).
# Therefore, the overall time complexity is O(n).

# Space Complexity (SC):
# 1. The space complexity is O(1) since we are only using a few extra pointers (n1, n2, p) and not creating any additional data structures.
# Therefore, the space complexity is O(1).
