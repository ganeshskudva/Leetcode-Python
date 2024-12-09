# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes to reverse
        node, cnt = head, 0
        while cnt < k:
            if not node:  # If fewer than k nodes remain, no reversal is done
                return head
            node = node.next
            cnt += 1
        
        # Recursively reverse the rest of the list in groups of k
        prev = self.reverseKGroup(node, k)
        
        # Reverse the current group of k nodes
        while cnt:
            nxt = head.next  # Store the next node
            head.next = prev  # Reverse the current node's pointer
            prev = head  # Move the prev pointer forward
            head = nxt  # Move the head pointer forward
            cnt -= 1  # Decrement the count of nodes left in the group
        
        # Return the new head of the reversed group
        return prev

# Time Complexity (TC):
# 1. Each node is visited exactly once to determine whether there are at least k nodes for reversal.
#    - This step is performed in O(n), where n is the total number of nodes.
# 2. Each node is part of exactly one reversal operation.
#    - For each group of k nodes, the reversal takes O(k) time.
#    - Since there are approximately n/k groups, the total time for reversal is O(n).
# 3. The recursive calls process the groups one by one, but no extra traversal occurs due to recursion.
# Overall Time Complexity: O(n), where n is the total number of nodes in the list.

# Space Complexity (SC):
# 1. The recursion depth is determined by the number of groups, which is approximately n/k.
#    - Each recursive call adds a frame to the stack.
# 2. No additional data structures are used, only a constant amount of extra space for variables (`node`, `cnt`, `prev`, `head`, etc.).
# Overall Space Complexity: O(n/k), where n is the total number of nodes and k is the group size.
