class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate minimum swaps required to sort an array
        def minSwaps(arr):
            n = len(arr)
            
            # Create a list of tuples containing the original indices and values
            arrpos = [*enumerate(arr)]
            
            # Sort the array by value while keeping track of original indices
            arrpos.sort(key=lambda it: it[1])
            
            # Create a visited dictionary to track whether an index has been processed
            vis = {k: False for k in range(n)}
            
            ans = 0  # Initialize the swap count
            
            # Iterate through the array to find cycles
            for i in range(n):
                # If the element is already visited or already in the correct position, skip it
                if vis[i] or arrpos[i][0] == i:
                    continue
                
                # Calculate the size of the cycle
                cycle_size = 0
                j = i
                
                while not vis[j]:
                    vis[j] = True
                    j = arrpos[j][0]  # Move to the next index in the cycle
                    cycle_size += 1
                
                # Add (cycle size - 1) to the total swaps if cycle size > 1
                if cycle_size > 0:
                    ans += (cycle_size - 1)
            
            return ans

        # Perform level-order traversal (BFS) of the tree
        queue = [root]  # Initialize queue with the root node
        ans = 0  # Total operations to sort all levels
        
        while queue:
            lst = []  # Store the values of the current level
            
            # Process all nodes at the current level
            for i in range(len(queue)):
                temp = queue.pop(0)  # Dequeue the front node
                lst.append(temp.val)  # Add its value to the level list
                
                # Enqueue left and right children if they exist
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            
            # If the level has more than one node, calculate minimum swaps
            if len(lst) > 1:
                ans += minSwaps(lst)  # Add minimum swaps required for this level
        
        return ans

# Time Complexity (TC):
# - minSwaps: O(n log n), where n is the number of elements in the array (level size).
# - Level-Order Traversal: O(V), where V is the number of nodes in the tree.
# - Overall: O(V log W), where W is the maximum width (number of nodes) at any level of the tree.

# Space Complexity (SC):
# - minSwaps: O(n), for the arrpos array and vis dictionary.
# - Level-Order Traversal: O(W), where W is the maximum width of the tree.
# - Overall: O(W), as the queue dominates the space usage.
