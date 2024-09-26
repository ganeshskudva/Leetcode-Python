from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store the events in sorted order
        self.events = []  # Each event is stored as a tuple (start, end)

    def book(self, start: int, end: int) -> bool:
        """
        Try to book a new event with the given start and end time.
        Return True if the event can be booked without overlap, otherwise return False.
        """
        
        # Use binary search to find the position where the new event (start, end) 
        # could be inserted to maintain sorted order. `bisect_left` gives the first
        # position where (start, end) can be inserted while maintaining order.
        i = bisect_left(self.events, (start, end))

        # Check for overlap with the previous event (if any)
        # If there's a previous event (i > 0) and its end time is greater than the 
        # new event's start time, it means the new event overlaps with the previous one.
        if i > 0 and self.events[i - 1][1] > start:
            return False  # Overlap with the previous event, booking fails

        # Check for overlap with the next event (if any)
        # If there's a next event (i < len(self.events)) and its start time is less than 
        # the new event's end time, it means the new event overlaps with the next one.
        if i < len(self.events) and self.events[i][0] < end:
            return False  # Overlap with the next event, booking fails

        # If there is no overlap, insert the new event at position `i`
        # This ensures that the list remains sorted after insertion
        self.events.insert(i, (start, end))
        
        # Successfully booked, return True
        return True
