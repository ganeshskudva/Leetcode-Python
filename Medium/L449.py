class Codec:

    # Encodes a tree to a single string using closure.
    def serialize(self, root):
        # `sb` will store the serialized values of the nodes
        sb = []

        # Closure function for recursion (helper function) to build the serialized string
        def solve(node):
            if node is None:
                return
            # Append the current node's value to the result list
            sb.append(str(node.val))
            # Recurse to serialize the left subtree
            solve(node.left)
            # Recurse to serialize the right subtree
            solve(node.right)

        # Call the closure starting from the root node
        solve(root)

        # Return the serialized tree as a comma-separated string
        return ','.join(sb)

    # Decodes the encoded string back to a binary tree using closure.
    def deserialize(self, data):
        if not data:
            return None

        # Create a deque (double-ended queue) of node values from the serialized data
        q = collections.deque(data.split(","))

        # Closure function for recursive deserialization
        def solve(lower=float('-inf'), upper=float('inf')):
            # If the queue is empty, return None (base case)
            if not q:
                return None

            # Peek at the next value in the queue
            val = int(q[0])

            # If the value is out of the bounds for a BST (lower, upper), return None
            if val < lower or val > upper:
                return None

            # Pop the value from the queue and create a new TreeNode
            q.popleft()
            root = TreeNode(val)

            # Recursively build the left subtree with updated bounds
            root.left = solve(lower, val)

            # Recursively build the right subtree with updated bounds
            root.right = solve(val, upper)

            return root

        # Call the closure starting with the root and the full bounds of possible values
        return solve()