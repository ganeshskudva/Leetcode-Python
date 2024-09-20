class Solution:
    def mostBooked(self, n: int, meets: List[List[int]]) -> int:
        # Array to keep track of how many times each room is booked
        cnt = [0] * n

        # Sort the meetings by start time
        meets.sort()

        # Priority queue (min-heap) for available rooms
        # Initially, all rooms are available
        avail = [i for i in range(n)] 
        heapq.heapify(avail)
        
        # Priority queue (min-heap) for busy rooms (stores a tuple of (end time, room index))
        busy = []

        # Process each meeting in the sorted list of meetings
        for m in meets:
            # While there are rooms in the busy queue, and the earliest room's end time is <= the current meeting's start time
            # Move that room back to the available queue
            while busy and busy[0][0] <= m[0]:
                heappush(avail, heappop(busy)[1])

            # Determine the start time for the current meeting
            start = m[0] if avail else busy[0][0]  
            # If no rooms are available, take the earliest end time from the busy rooms
            duration = m[1] - m[0]  # Calculate the meeting duration

            # Assign a room: either from the available queue, or from the earliest finishing busy room
            if avail:
                room = heappop(avail)  # Take the available room
            else:
                room = heappop(busy)[1]  # Take the room that becomes available earliest

            # Increment the booking count for the room
            cnt[room] += 1

            # Add the room to the busy queue with its new end time
            heappush(busy, (start + duration, room))

        # Return the room with the maximum bookings (in case of ties, return the room with the smallest index)
        return cnt.index(max(cnt))