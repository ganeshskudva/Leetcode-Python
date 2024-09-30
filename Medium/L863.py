class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Initialize an empty list 'res' to store the result (nodes at distance k)
        # and a defaultdict 'mp' to store the distance of nodes from the target node.
        res, mp = [], defaultdict(int)

        # The 'find' function is used to find the target node and record the distances
        # of all ancestor nodes from the target node.
        def find(node):
            # Base case: if the current node is None (reached the end of a path), return.
            if not node:
                return

            # If the current node is the target node, store its distance as 0 in 'mp'
            # because the distance of the target from itself is 0.
            if node == target:
                mp[node] = 0
                return

            # Recursively call 'find' on the left child to search for the target in the left subtree.
            find(node.left)
            # If the target is found in the left subtree (i.e., node.left is in 'mp'),
            # set the distance of the current node to be one more than its left child.
            if node.left in mp:
                mp[node] = mp[node.left] + 1
                return

            # Recursively call 'find' on the right child to search for the target in the right subtree.
            find(node.right)
            # If the target is found in the right subtree (i.e., node.right is in 'mp'),
            # set the distance of the current node to be one more than its right child.
            if node.right in mp:
                mp[node] = mp[node.right] + 1
                return

        # The 'search' function is used to find nodes that are at the required distance 'k'
        # from the target node. It traverses the tree and checks for nodes at the correct distance.
        def search(node, dist=0):
            # Base case: if the current node is None, return.
            if not node:
                return

            # If the current node is an ancestor (or target) that we found using the 'find' function,
            # set the distance to the value stored in 'mp' for that node.
            if node in mp:
                dist = mp[node]

            # If the distance of the current node is exactly 'k', add the node's value to the result list.
            if dist == k:
                res.append(node.val)

            # Recursively search the left child, increasing the distance by 1.
            search(node.left, dist + 1)
            # Recursively search the right child, increasing the distance by 1.
            search(node.right, dist + 1)

        # Call 'find' to locate the target node and record the distances of all its ancestors.
        find(root)
        # Call 'search' to traverse the tree and find all nodes at distance 'k' from the target.
        search(root)

        # Return the result list containing all nodes at distance 'k' from the target node.
        return res
