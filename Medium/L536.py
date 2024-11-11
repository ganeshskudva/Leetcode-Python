class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # If input string is empty, return None (no tree to construct)
        if not s:
            return None

        # Stack to maintain the tree nodes while constructing the tree
        stack = deque()
        i = 0  # Pointer for the start of the current number

        while i < len(s):
            # Process closing parenthesis which indicates the end of a subtree
            if s[i] == ')':
                stack.pop()
                i += 1

            # Process digits or a negative sign, which indicates the start of a number
            elif s[i].isdigit() or s[i] == '-':
                j = i
                # Move i to capture the entire number
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                # Create a new tree node with the parsed integer value
                current_node = TreeNode(int(s[j:i + 1]))

                # If the stack is not empty, the top node in the stack is the parent of the current node
                if stack:
                    parent = stack[-1]
                    # Attach current_node as the left child if it's vacant, otherwise as the right child
                    if not parent.left:
                        parent.left = current_node
                    else:
                        parent.right = current_node

                # Push the current node onto the stack to allow adding children
                stack.append(current_node)
                i += 1  # Move to the next character after processing the number

            # Skip open parenthesis since it only indicates the start of a new subtree
            else:
                i += 1

        # The root of the tree is the first element in the stack
        return stack[0] if stack else None

# Time Complexity (TC):
# - We iterate through each character of the input string once, making this O(N) where N is the length of the string.
# - Parsing each number and pushing/popping from the stack are O(1) operations, so the overall time complexity remains O(N).

# Space Complexity (SC):
# - In the worst case, the stack can hold all nodes at a particular depth of the tree, leading to O(H) space complexity,
#   where H is the height of the tree. For a balanced tree, H = O(log N), but in the worst case (e.g., a skewed tree), H = O(N).
# - The final tree structure itself requires O(N) space to store the nodes.
# - Therefore, the overall space complexity is O(N).