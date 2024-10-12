from heapq import heappop, heappush
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Create a priority queue (min-heap) to track the end times of intervals.
        pq = []

        # Sort intervals based on their start times (left).
        for left, right in sorted(intervals):
            # If there is an interval in the heap and its end time is less than the current start time,
            # it means that the previous interval has finished, so we can reuse that group.
            if pq and pq[0] < left:
                # Remove the interval with the earliest end time from the heap.
                heappop(pq)
            
            # Add the current interval's end time to the heap.
            heappush(pq, right)

        # The size of the heap at the end will be the minimum number of groups needed.
        # Each group represents overlapping intervals that need to be in the same group.
        return len(pq)

# Time Complexity (TC):
# 1. Sorting the intervals takes O(n log n), where n is the number of intervals.
# 2. Iterating over the intervals and performing heap operations (heappop and heappush) for each interval:
#    - Each heap operation takes O(log k), where k is the number of intervals in the heap at any point.
#    - In the worst case, the heap could contain all n intervals, so the heap operations take O(log n).
#    - Therefore, iterating through all intervals with heap operations takes O(n log n).
# Overall, the time complexity is O(n log n).

# Space Complexity (SC):
# 1. The space needed to store the sorted intervals is O(n).
# 2. The heap can grow up to the size of n intervals in the worst case, which takes O(n) space.
# Therefore, the overall space complexity is O(n).
