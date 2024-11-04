class SeatManager:

    def __init__(self, n: int):
        # Initialize the next available seat pointer and a set for unreserved seats
        # Time Complexity for initialization: O(1)
        # Space Complexity: O(n) to store up to n seat numbers if all are unreserved
        self.next_seat = 1
        self.unreserved_seats = set()  # Track unreserved seats explicitly

    def reserve(self) -> int:
        # Reserve the smallest available seat number
        # If there are unreserved seats, pick the smallest one (O(1) amortized)
        # Otherwise, use the next seat in sequence (O(1))
        # Time Complexity: O(1) amortized
        if self.unreserved_seats:
            seat = min(self.unreserved_seats)  # O(1) amortized if set allows fast min retrieval
            self.unreserved_seats.remove(seat)  # O(1) on average to remove from set
        else:
            # If no unreserved seats, use the next available seat
            seat = self.next_seat
            self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        # Mark a seat as available by adding it back to the unreserved seats set
        # Time Complexity: O(1) on average for adding to the set
        self.unreserved_seats.add(seatNumber)

# Overall Time Complexity:
# - reserve(): O(1) amortized due to incrementing `next_seat` and constant-time set operations
# - unreserve(): O(1) on average due to set addition

# Overall Space Complexity:
# - O(n), where `n` is the total number of seats, as the set can hold up to n unreserved seats
