from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Step 1: Initialize the result array `res` with zeroes of length `n`, where `n` is the number of flights.
        res = [0] * n

        # Step 2: Process each booking in the `bookings` list.
        # Each booking contains three values: `first`, `last`, and `seats`.
        for first, last, seats in bookings:
            # Increment the seats at the index `first - 1` to mark the start of the seat reservation.
            res[first - 1] += seats

            # If `last` is within the bounds, decrement the seats at index `last` to mark the end of the reservation.
            if last < n:
                res[last] -= seats

        # Step 3: Accumulate the seat reservations to get the final number of seats booked on each flight.
        # This step propagates the seat counts across the flights.
        for i in range(1, n):
            res[i] += res[i - 1]

        # Step 4: Return the result array which now contains the final number of seats booked on each flight.
        return res

# Time Complexity (TC):
# 1. Initializing the `res` array takes O(n) time, where `n` is the number of flights.
# 2. Processing the `bookings` array takes O(u) time, where `u` is the number of bookings. 
#    Each booking is processed in constant time, with two updates to the `res` array.
# 3. The accumulation step (updating the seat count for each flight) takes O(n) time, since we loop through all `n` flights.
# 
# Therefore, the overall time complexity is O(n + u), where `n` is the number of flights and `u` is the number of bookings.

# Space Complexity (SC):
# 1. The `res` array is of size `n`, which requires O(n) space.
# 2. We do not use any additional significant data structures, aside from some loop variables, which take constant space (O(1)).
# 
# Therefore, the overall space complexity is O(n).
