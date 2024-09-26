from bisect import bisect_left

class MyCalendarTwo:

    def __init__(self):
        # Initialize two lists:
        # `events` stores all single bookings as tuples (start, end)
        # `overlaps` stores intervals where two bookings overlap (double bookings)
        self.events = []  
        self.overlaps = []  

    def book(self, start: int, end: int) -> bool:
        # Step 1: Check for any triple bookings (overlaps with existing double bookings)
        for s, e in self.overlaps:
            # A triple booking happens if the new event overlaps with an already double-booked interval
            if not (end <= s or start >= e):  # No overlap if (new_end <= existing_start) or (new_start >= existing_end)
                return False  # Triple booking detected, reject the booking

        # Step 2: Check for any new double bookings with existing single bookings
        for s, e in self.events:
            # Check if the new event overlaps with an existing event
            if not (end <= s or start >= e):  # No overlap if (new_end <= existing_start) or (new_start >= existing_end)
                # If there's an overlap, calculate the overlapping interval (start of the max, end of the min)
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                # Add this overlapping interval to the `overlaps` list (marking a new double booking)
                self.overlaps.append((overlap_start, overlap_end))

        # Step 3: If no triple booking is detected, book the new event by adding it to the `events` list
        self.events.append((start, end))  # Add the new event to the list of single bookings
        return True  # Successfully booked the event
