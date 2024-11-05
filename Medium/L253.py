from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by their start times to process meetings in chronological order
        intervals.sort()

        # Initialize a min-heap to keep track of end times of ongoing meetings
        hp = []

        # Iterate over each meeting interval
        for start, end in intervals:
            # If there's a room that gets free (the meeting with the earliest end time ends before this one starts),
            # free it up by popping the earliest end time from the heap
            if hp and hp[0] <= start:
                heapq.heappop(hp)

            # Push the current meeting's end time onto the heap
            heapq.heappush(hp, end)

        # The size of the heap tells us the minimum number of meeting rooms required
        return len(hp)

# Time Complexity (TC): O(n log n)
#   - Sorting the intervals by start times takes O(n log n).
#   - For each interval, we perform a `heappush` and possibly a `heappop`, both of which are O(log n).
#   - This results in an overall time complexity of O(n log n).

# Space Complexity (SC): O(n)
#   - In the worst case, all meetings could overlap, requiring a separate room for each.
#   - Thus, the heap can grow up to size n in the worst case, resulting in an O(n) space complexity.
