class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # Variables to keep track of the maximum score and the count of nodes with that score
        max_score = float('-inf')
        cnt = 0
        n = len(parents)
        mp = defaultdict(list)

        # Build the tree: map each parent to its children
        for i in range(1, n):
            mp[parents[i]].append(i)
        
        # Recursive function to calculate subtree sizes and scores
        def solve(node=0):
            nonlocal max_score, cnt  # Access nonlocal variables in the nested function
            tot = 0  # Total nodes in the current subtree
            prod = 1  # Product of the sizes of child subtrees
            
            # Traverse all children (subtrees) of the current node
            for nei in mp[node]:
                child_size = solve(nei)
                tot += child_size
                prod *= child_size

            # Calculate remaining nodes outside the current subtree (total nodes - subtree size - 1)
            rem = n - tot - 1
            if rem > 0:
                prod *= rem
            
            # Update max_score and cnt accordingly
            if prod > max_score:
                max_score = prod
                cnt = 1  # Reset count to 1 as a new max score is found
            elif prod == max_score:
                cnt += 1  # Increment count for nodes with the same max score
            
            return tot + 1  # Return the size of the subtree rooted at this node (including itself)

        # Start the recursive traversal from the root node (0)
        solve()
        
        # Return the count of nodes with the highest score
        return cnt
