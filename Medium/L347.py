from collections import Counter
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in `nums`
        count = Counter(nums)  # O(n), where n is the length of nums

        # Step 2: Use a min-heap to keep only the top k elements
        heap = []
        
        # Push each element with its frequency into the heap
        for num, freq in count.items():  # O(m), where m is the number of unique elements
            heappush(heap, (freq, num))  # Push the element with frequency as the key
            if len(heap) > k:  # If the heap size exceeds k, pop the smallest frequency element
                heappop(heap)
        
        # Step 3: Extract the elements from the heap
        return [num for freq, num in heap]

# Time Complexity (TC): O(n + m log k), where:
# - O(n) is the time to count the frequency of elements in `nums`.
# - O(m log k) is the time to maintain a heap of size k, where m is the number of unique elements.
#   Each heappush and heappop operation takes O(log k), and we perform these operations m times.

# Space Complexity (SC): O(m + k), where:
# - O(m) is the space for the frequency counter, which stores up to m unique elements.
# - O(k) is the space for the min-heap, which keeps only the top k elements.
