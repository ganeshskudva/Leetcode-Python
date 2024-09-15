# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Initialize an empty list to store the serialized values (sb = string builder)
        sb = []

        # Closure (helper function) to perform the recursive serialization
        def solve(node):
            # If the current node is None, add a placeholder '#' to indicate null
            if not node:
                sb.append('#,')  # Use '#' to represent null nodes, followed by a comma
            else:
                # Append the node's value, followed by a comma
                sb.append(str(node.val))
                sb.append(',')
                # Recursively serialize the left and right subtrees
                solve(node.left)
                solve(node.right)

        # Start the recursive serialization from the root node
        solve(root)

        # Join the list of strings into a single serialized string and return it
        return ''.join(sb)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Convert the serialized string into a deque of values using commas as delimiters
        # The deque allows efficient popping from the front
        q = deque(data.split(","))

        # Closure (helper function) to perform recursive deserialization
        def solve():
            # Pop the next value from the deque
            val = q.popleft()

            # If the value is '#', it represents a null node, so return None
            if val == '#':
                return None

            # Otherwise, convert the value to an integer and create a new TreeNode
            root = TreeNode(int(val))

            # Recursively deserialize the left and right subtrees and attach them to the current node
            root.left = solve()  # Recurse for the left subtree
            root.right = solve()  # Recurse for the right subtree

            # Return the reconstructed tree node
            return root

        # Start the deserialization process and return the root of the reconstructed tree
        return solve()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))