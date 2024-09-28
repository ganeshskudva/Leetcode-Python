class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Return 0 if the weights list is empty (defensive handling)
        if not weights:
            return 0

        # Helper function to check if it's possible to ship within the given days with max_weight capacity
        def is_feasible(max_weight):
            current_load = 0  # Tracks the current load for the day
            day_count = 1  # Start with the first day

            for w in weights:
                # If adding the current weight exceeds max_weight, start a new day
                if current_load + w > max_weight:
                    day_count += 1  # Increment the day count
                    current_load = w  # Start the new day with the current weight
                    if day_count > days:
                        return False  # If days exceed the allowed limit, return False
                else:
                    current_load += w  # Accumulate the weight in the current day's load

            return True  # If we successfully fit everything in the allowed days, return True

        # Binary search range: the min capacity is max(weights) (ship must carry the heaviest package),
        # and the max capacity is sum(weights) (ship can carry all weights in one day).
        low, high = max(weights), sum(weights)

        # Perform binary search to find the minimum feasible ship capacity
        while low < high:
            mid = low + (high - low) // 2  # Midpoint of the current capacity range

            # If the current mid capacity is feasible, try a smaller capacity
            if is_feasible(mid):
                high = mid  # Look for smaller capacities
            else:
                low = mid + 1  # Increase the capacity since the current one is too small

        # When the loop ends, low will be the smallest feasible capacity
        return low
