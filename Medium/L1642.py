class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Initialize a min-heap to track the largest jumps we've used bricks on
        # Space Complexity: O(ladders) as we store at most `ladders` elements in the heap
        hp = []
        
        # Traverse through each building, calculating the difference in heights
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            
            # If there's an upward jump (height difference > 0)
            if d > 0:
                # Push the height difference into the min-heap
                # Time Complexity: O(log ladders) for each push operation
                heapq.heappush(hp, d)
            
            # If the heap size exceeds the number of ladders, we use bricks for the smallest jump
            if len(hp) > ladders:
                # Pop the smallest jump and reduce the number of bricks by that amount
                # Time Complexity: O(log ladders) for each pop operation
                bricks -= heapq.heappop(hp)
            
            # If we run out of bricks, we return the current index as the furthest building reached
            if bricks < 0:
                return i
        
        # If we complete the loop, we can reach the last building
        return len(heights) - 1

# Overall Time Complexity: O(n log ladders), where n is the number of buildings
# Overall Space Complexity: O(ladders) for the heap
