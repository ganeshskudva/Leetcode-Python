class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of projects with their capital and profit
        projects = zip(capital, profits)

        # # Min-heap for capital requirements
        min_heap = []
        for project in projects:
            heapq.heappush(min_heap, project)

        # Max-heap for profits (use negative profits to simulate max-heap in Python)
        max_heap = []

        # Iterate for at most k projects
        for _ in range(k):
            # Move all projects that can be afforded with the current capital to the max-heap
            while min_heap and min_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -prof)

            # If there are no more projects we can afford, break the loop
            if not max_heap:
                break

            # Select the project with the maximum profit
            w += -heapq.heappop(max_heap)

        return w
