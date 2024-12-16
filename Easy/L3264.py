from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if not nums:
            return []

        # Create a heap with tuples (value, index) and heapify
        min_heap = [(value, idx) for idx, value in enumerate(nums)]
        heapify(min_heap)  # O(n) to build the heap

        # Perform k operations: multiply the smallest element and push it back
        for _ in range(k):
            value, idx = heappop(min_heap)  # O(log n) to extract the smallest element
            heappush(min_heap, (value * multiplier, idx))  # O(log n) to push updated element

        # Reconstruct the result array based on the final heap state
        result = [0] * len(nums)
        while min_heap:
            value, idx = heappop(min_heap)  # O(log n) for each pop
            result[idx] = value  # Place the value in the original index

        return result

# Time Complexity (TC):
# 1. Heapify: O(n), where n is the number of elements in nums.
# 2. `k` heap operations (pop and push): O(k * log n).
# 3. Reconstructing the result array: O(n * log n) to extract elements from the heap.
# Overall TC: O(n + k * log n + n * log n) ≈ O((k + n) * log n).

# Space Complexity (SC):
# 1. Min-heap stores n elements: O(n).
# 2. Result array stores n elements: O(n).
# 3. Auxiliary variables and function stack: O(1).
# Overall SC: O(n).
