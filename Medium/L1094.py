## non heap based solution

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Dictionary to track the change in passengers at each time point
        timeline = {}

        # For each trip, record the number of passengers to add at the start and remove at the end
        for passengers, start, end in trips:
            # Increment passengers at the start of the trip
            if start in timeline:
                timeline[start] += passengers
            else:
                timeline[start] = passengers
            
            # Decrement passengers at the end of the trip
            if end in timeline:
                timeline[end] -= passengers
            else:
                timeline[end] = -passengers

        # Sort the timeline by time (this ensures we're processing events in the correct order)
        sorted_times = sorted(timeline.items())

        current_passengers = 0

        # Traverse through the timeline to simulate the carpool process
        for time, passenger_change in sorted_times:
            current_passengers += passenger_change

            # If at any point, the current passengers exceed capacity, return False
            if current_passengers > capacity:
                return False

        # If we never exceed capacity, return True
        return True

# Time Complexity (TC):
# 1. For building the timeline:
#    - We go through each trip once, so this step takes O(n), where n is the number of trips.
# 2. Sorting the timeline:
#    - The timeline consists of at most 2n unique time points (each trip contributes at most 2 points: start and end).
#    - Sorting these time points takes O(m log m), where m is the number of unique time points.
#    - In the worst case, m = 2n, so sorting takes O(n log n).
# 3. Traversing the sorted timeline:
#    - We traverse the sorted timeline once, which takes O(m), or O(n) in the worst case.
# 
# Thus, the overall time complexity is O(n log n), dominated by sorting the timeline.

# Space Complexity (SC):
# 1. The timeline dictionary contains at most 2n entries (one for the start and one for the end of each trip), so it requires O(n) space.
# 2. The sorted list of timeline entries also requires O(n) space.
# 
# Thus, the overall space complexity is O(n).


## heap based solution

from heapq import heappop, heappush
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Sort trips by start time
        trips.sort(key=lambda x: x[1])  # Sort by the start time of each trip

        # Step 2: Min-heap to track when passengers will be dropped off
        heap = []
        current_passengers = 0

        # Step 3: Process each trip
        for passengers, start, end in trips:
            # Remove trips from the heap that have already ended
            while heap and heap[0][0] <= start:
                # Subtract the passengers of the completed trip from the current passengers
                current_passengers -= heappop(heap)[1]

            # Add the current trip's passengers
            current_passengers += passengers

            # Check if capacity is exceeded
            if current_passengers > capacity:
                return False

            # Add the current trip's end time and number of passengers to the heap
            heappush(heap, (end, passengers))

        # If we processed all trips without exceeding capacity, return True
        return True

# Time Complexity (TC):
# 1. Sorting the trips takes O(n log n), where n is the number of trips.
# 2. Each trip is processed once, and for each trip:
#    - We push the trip into the heap, which takes O(log k), where k is the number of elements in the heap.
#    - We pop trips from the heap as they end, which also takes O(log k).
#    Since k (the heap size) is bounded by the number of overlapping trips, in the worst case, k = n.
#    Therefore, the total time complexity for the heap operations is O(n log n).
# 3. Overall, the time complexity is dominated by sorting and heap operations, so the time complexity is O(n log n).

# Space Complexity (SC):
# 1. The heap can grow to the size of n trips in the worst case (if all trips overlap), so the heap requires O(n) space.
# 2. The space required for storing the sorted list of trips is also O(n).
# 3. Overall, the space complexity is O(n), primarily due to the heap.
