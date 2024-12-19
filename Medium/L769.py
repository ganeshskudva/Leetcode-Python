class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize chunks counter to 0 and cur_max to negative infinity
        chunks, cur_max = 0, -inf
        
        # Iterate through the array with both index and value
        for i, num in enumerate(arr):
            # Update cur_max to the maximum value seen so far
            cur_max = max(cur_max, num)
            # If the maximum value matches the current index, increment chunks
            if cur_max == i:
                chunks += 1
        
        # Return the total number of chunks
        return chunks

# Time Complexity (TC): O(n), where n is the length of the array. 
# We iterate through the array once, performing O(1) operations per element.

# Space Complexity (SC): O(1).
# We use a constant amount of extra space for variables (chunks and cur_max).
