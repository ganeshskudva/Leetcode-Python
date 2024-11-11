# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case: if the head is None, return None
        if not head:
            return None

        # Base case: if there is only one node, return it as a TreeNode
        if not head.next:
            return TreeNode(head.val)

        # Use two pointers, `slow` and `fast`, to find the middle of the list
        slow, fast = head, head
        prev = None  # To keep track of the node before `slow`
        
        # Move `slow` to the middle and `fast` to the end
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # `slow` is now pointing to the middle node, which will be the root of the BST
        # Disconnect the left half from the middle
        if prev:
            prev.next = None

        # Create the root node of the BST with the value of the middle node
        root = TreeNode(slow.val)

        # Recursively build the left and right subtrees
        root.left = self.sortedListToBST(head)  # Left half of the list
        root.right = self.sortedListToBST(slow.next)  # Right half of the list

        return root

# Time Complexity (TC):
# - Finding the middle node takes O(N) for each recursive call, where N is the number of nodes in the current list.
# - Since we split the list into halves in each recursive call, this results in O(N log N) complexity overall.

# Space Complexity (SC):
# - The recursion depth is O(log N) for a balanced BST, where N is the number of nodes in the list.
# - However, each recursive call creates a new TreeNode, resulting in O(N) space for the tree structure.
# - The additional space complexity for the recursion stack is O(log N), so overall space complexity is O(N).
