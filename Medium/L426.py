class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # If the tree is empty, return None.
        if not root:
            return None

        # Helper function to merge two circular doubly linked lists.
        def connect(n1, n2):
            if not n1:  # If the first list is empty, return the second list.
                return n2
            if not n2:  # If the second list is empty, return the first list.
                return n1

            # Find the tails of both lists.
            tail1, tail2 = n1.left, n2.left

            # Connect the tail of the first list to the head of the second.
            tail1.right = n2
            n2.left = tail1

            # Connect the tail of the second list to the head of the first.
            tail2.right = n1
            n1.left = tail2

            # Return the head of the merged list.
            return n1

        # Recursively convert the left and right subtrees to circular DLLs.
        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)

        # Make the root node a single-node circular DLL.
        root.left = root.right = root

        # Merge left subtree DLL, root node, and right subtree DLL.
        return connect(connect(left_head, root), right_head)

# Time Complexity (TC): O(n)
# - Each node in the BST is visited exactly once.
# Space Complexity (SC): O(h)
# - Recursion stack space depends on the height of the tree (O(log n) for balanced trees, O(n) for skewed trees).
