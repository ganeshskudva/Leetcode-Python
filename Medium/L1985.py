from typing import List
import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Initialize a min-heap to store the k largest numbers
        minHeap = []
        
        # Process each number in the list
        for x in nums:
            # Convert the number to integer and push it into the min-heap
            # Time Complexity: O(log k) for each heappush operation when heap size is k
            heapq.heappush(minHeap, int(x))
            
            # If the heap size exceeds k, remove the smallest element to maintain only k largest numbers
            if len(minHeap) > k:
                # Time Complexity: O(log k) for each heappop operation
                heapq.heappop(minHeap)
        
        # The root of the heap (minHeap[0]) is now the k-th largest number
        # Convert it back to a string to match the return type
        return str(minHeap[0])

# Overall Time Complexity: O(n log k)
#   - Each element is pushed into the heap, and for any excess beyond k elements, the smallest is popped.
#   - Thus, each push/pop operation on the heap takes O(log k) time, resulting in O(n log k) for n elements.

# Overall Space Complexity: O(k)
#   - The heap maintains only k elements at any time, resulting in a space complexity of O(k).
