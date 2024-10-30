class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate the weights of the stones to simulate a max heap using Python's min-heap
        hp = [-s for s in stones]
        # Heapify the list to build the initial heap
        heapify(hp)

        # Continue until there is at most one stone left
        while len(hp) >= 2:
            # Pop the two largest stones (negated values give the largest in the max heap)
            first, sec = heappop(hp), heappop(hp)
            # If they are not equal, push the difference back into the heap
            if first != sec:
                heappush(hp, -abs(first - sec))

        # If there's one stone left, return its weight (negate to get positive value)
        # If no stones are left, return 0
        return -hp[0] if hp else 0

# Time Complexity (TC): O(n log n), where n is the number of stones.
# - Building the heap takes O(n).
# - Each iteration in the while loop involves two pop operations and possibly one push operation, each O(log n).
# - The loop runs O(n) times in the worst case, so the overall TC is O(n log n).

# Space Complexity (SC): O(n), where n is the number of stones.
# - The heap (hp) requires O(n) space to store the negated stone weights.
