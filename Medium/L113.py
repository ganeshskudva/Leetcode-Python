# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []  # List to store all valid paths

        def solve(node, tgt=0, tmp=[]):
            # Base case: If the node is None, return
            if not node:
                return
            
            # Add the current node's value to the temporary path
            tmp.append(node.val)

            # Check if the current node is a leaf and the target sum matches
            if tgt == node.val and not node.left and not node.right:
                res.append(list(tmp))  # Append a copy of the current path to the result
            
            # Recur for the left and right children with updated target sum
            solve(node.left, tgt - node.val, tmp)
            solve(node.right, tgt - node.val, tmp)
            
            # Backtrack: Remove the current node's value from the path
            del tmp[-1]

        # Start the recursive function with the root and the target sum
        solve(root, targetSum)
        return res

# Time Complexity (TC): O(n)
# - Each node is visited exactly once, where n is the total number of nodes in the tree.
# - The list operations (appending and deleting) take O(1) on average.
# - The total time complexity is O(n).

# Space Complexity (SC): O(h)
# - The recursion stack can go as deep as the height of the tree (h).
# - The temporary list `tmp` can also hold up to h elements in the worst case.
# - In the worst case of a skewed tree, h = n, making the space complexity O(n).
# - In the best case of a balanced tree, h = log(n), making the space complexity O(log(n)).

