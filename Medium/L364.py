class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Edge case: If the input nested list is empty, return 0
        if not nestedList:
            return 0
        
        # `single_sum` accumulates integers at the current depth
        # `tot` accumulates the weighted sum of integers at all depths
        # `q` is a deque used for level-order traversal (BFS)
        single_sum, tot, q = 0, 0, deque([nestedList])
        
        # Perform level-order traversal (BFS)
        while q:
            # Number of elements at the current level
            sz = len(q)
            
            # Process each element at the current level
            for _ in range(sz):
                # Dequeue an element (a NestedInteger object or list)
                node = q.popleft()
                
                # Iterate through each NestedInteger in the dequeued element
                for ni in node:
                    if ni.isInteger():
                        # Add integer value to the current depth sum
                        single_sum += ni.getInteger()
                    else:
                        # Enqueue the nested list for processing at the next depth
                        q.append(ni.getList())
            
            # Accumulate the running total weighted by depth
            tot += single_sum
        
        # Return the total weighted sum
        return tot

# Time Complexity (TC):
# Let n be the total number of integers and nested lists in `nestedList`.
# Each NestedInteger object is visited exactly once in the BFS traversal.
# Thus, the time complexity is O(n).

# Space Complexity (SC):
# The space complexity depends on the maximum width of the nested structure,
# which is the maximum number of elements at any single depth.
# In the worst case, all elements could be at the same level, requiring O(n) space for the deque.
# Thus, the space complexity is O(n).
