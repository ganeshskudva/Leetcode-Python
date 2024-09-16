class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Create a set to store the minutes in a day (1440 minutes total). This helps check for duplicates.
        st = set()

        # Convert each time string in timePoints to the total minutes since 00:00 (midnight).
        for t in timePoints:
            # Split the time string into hours and minutes, and convert them to integers.
            h, m = map(int, t.split(":"))
            # Calculate the total minutes from 00:00.
            total_minutes = h * 60 + m

            # If the time point already exists in the set, return 0 because duplicate times have a difference of 0.
            if total_minutes in st:
                return 0

            # Add the total minutes to the set for further processing.
            st.add(total_minutes)

        # Initialize the previous time in minutes, the minimum difference (mn), and track the first and last times.
        prev, mn = 0, float('inf')  # mn is initialized to infinity to find the minimum difference.
        first, last = float('inf'), float('-inf')  # first and last are initialized to extremes for comparison.

        # Iterate through all 1440 possible minutes in a day (24 hours * 60 minutes).
        for i in range(24 * 60):
            # If the minute `i` is present in the set (indicating it exists in timePoints):
            if i in st:
                # If we already encountered a time (first is updated), calculate the difference from the previous time.
                if first != float('inf'):
                    mn = min(mn, i - prev)  # Update the minimum difference.
                
                # Update the first, last, and prev values with the current minute i.
                first, last, prev = min(first, i), max(last, i), i

        # After looping, account for the circular difference between the last and first time points (across midnight).
        mn = min(mn, (24 * 60 - last + first))

        # Return the minimum time difference.
        return mn