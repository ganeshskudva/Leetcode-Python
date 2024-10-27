from collections import deque
from typing import List

class NestedInteger:
    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getInteger(self) -> int:
        """Return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list."""
        pass

    def getList(self) -> List['NestedInteger']:
        """Return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer."""
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        
        sum = 0  # Initialize sum to store weighted sum of integers
        level = 1  # Start from level 1
        queue = deque(nestedList)  # Initialize the queue with nestedList
        
        # Breadth-first traversal of each level
        while queue:
            size = len(queue)
            
            for _ in range(size):
                ni = queue.popleft()  # Dequeue the first element
                
                if ni.isInteger():
                    # If it's an integer, add the weighted integer to sum
                    sum += ni.getInteger() * level
                else:
                    # If it's a list, add all elements to the queue for the next level
                    queue.extend(ni.getList())
            
            level += 1  # Move to the next level after processing the current level
        
        return sum  # Return the total weighted sum of integers

# Time Complexity (TC): O(n), where n is the total number of integers and lists in `nestedList`.
# - Each NestedInteger is processed once in the queue, so the overall time is proportional to the number of elements.

# Space Complexity (SC): O(n), where n is the total number of integers and lists in `nestedList`.
# - The queue may hold up to all elements of `nestedList` at a given time, especially in the worst case where all elements are at the same depth level.
