#Line Sweep based 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Dictionary to store the net change in meetings at each time point
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1  # Increment count at the start of a meeting
            mp[end] -= 1    # Decrement count at the end of a meeting

        # Initialize variables to track the maximum overlap
        res, cnt = 0, 0
        # Process time points in chronological order
        for k in sorted(mp.keys()):
            cnt += mp[k]  # Update the running count of ongoing meetings
            res = max(res, cnt)  # Update the maximum number of overlapping meetings

        return res

# Time Complexity (TC):
# 1. Building the dictionary (`mp`): O(n), where n is the number of intervals.
#    - For each interval, two operations (start and end) are performed.
# 2. Sorting the keys of the dictionary: O(m log m), where m is the number of unique time points.
#    - In the worst case, m = 2n (one unique key for each start and end time).
# 3. Iterating over the sorted keys: O(m), where m is the number of unique time points.
# Overall TC: O(n) + O(m log m) + O(m) ≈ O(n log n), since m ≤ 2n.

# Space Complexity (SC):
# 1. Dictionary (`mp`): O(m), where m is the number of unique time points.
#    - In the worst case, m = 2n (one unique key for each start and end time).
# 2. Sorting keys: O(m), where m is the number of unique time points.
# 3. Additional variables (`res`, `cnt`): O(1).
# Overall SC: O(m) ≈ O(n), since m ≤ 2n.



# Heap based
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
