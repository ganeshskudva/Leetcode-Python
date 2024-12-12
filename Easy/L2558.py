class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Create a max-heap (using negative values since Python has a min-heap by default)
        hp = [-g for g in gifts]
        heapify(hp)  # O(n), where n is the number of elements in gifts

        # Perform k operations to replace the largest gift with the square root of its value
        for _ in range(k):
            # Extract the largest element (-heappop) and push the square root back into the heap
            heappush(hp, -math.floor(math.sqrt(-heappop(hp))))  # O(log n) for heappop and heappush

        # Return the sum of the heap elements converted back to positive
        return -sum(hp)  # O(n) for summing all elements

# Time Complexity (TC):
# - heapify takes O(n).
# - Each of the k operations involves a heappop and heappush, each taking O(log n), so O(k * log n).
# - Summing up the heap takes O(n).
# Total TC = O(n) + O(k * log n) + O(n) = O(n + k * log n)

# Space Complexity (SC):
# - The heap `hp` uses O(n) space.
# Total SC = O(n)
