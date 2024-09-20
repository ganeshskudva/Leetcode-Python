class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Initialize a min-heap to keep track of the end times of ongoing meetings
        hp = []

        # Sort the intervals by their start times. This ensures that we process meetings in chronological order.
        intervals.sort()

        # Iterate over each meeting interval
        for i in intervals:
            # If the heap is not empty and the current meeting can start after or when
            # the earliest ending meeting ends, replace the earliest ending meeting's end time.
            # This means the room can be reused, so we update the end time of the meeting in the heap.
            if hp and i[0] >= hp[0]:  # `i[0]` is the start time of the current meeting.
                heapq.heapreplace(hp, i[1])  # Replace the root of the heap with the current meeting's end time.
            else:
                # If the current meeting can't reuse any existing room, push its end time onto the heap,
                # indicating a new room is needed.
                heapq.heappush(hp, i[1])  # `i[1]` is the end time of the current meeting.

        # The size of the heap tells us the minimum number of meeting rooms required.
        return len(hp)