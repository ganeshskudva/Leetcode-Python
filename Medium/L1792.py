import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        # Define the profit function (marginal increase in pass ratio)
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        # Initialize a max-heap with negative profit for max-heap simulation
        maxHeap = [(-profit(a, b), a, b) for a, b in classes]
        heapq.heapify(maxHeap)  # Build the heap, O(N)

        # Distribute extra students
        for _ in range(extraStudents):
            # Pop the class with the maximum marginal profit
            maxProfit, a, b = heapq.heappop(maxHeap)
            # Add one extra student and recompute the profit
            a, b = a + 1, b + 1
            heapq.heappush(maxHeap, (-profit(a, b), a, b))  # Push the updated class, O(log N)

        # Calculate the average pass ratio
        return sum(a / b for _, a, b in maxHeap) / len(classes)

# Time Complexity (TC):
# 1. Initializing the heap: O(N), where N is the number of classes.
# 2. For each of the extraStudents:
#    - Heap pop operation: O(log N)
#    - Heap push operation: O(log N)
#    Total for heap operations: O(extraStudents * log N).
# 3. Calculating the final sum of ratios: O(N).
# Overall TC: O(N + extraStudents * log N).

# Space Complexity (SC):
# 1. The heap stores tuples for each class: O(N).
# 2. Auxiliary variables and function stack usage are negligible compared to the heap.
# Overall SC: O(N).
