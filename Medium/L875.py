class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If the list of piles is empty, there's no bananas to eat, so return 0
        if not piles:
            return 0

        # If we need to finish all piles in exactly one hour, the only option is to eat all bananas in that time
        if h == 1:
            return sum(piles)  # Eating all bananas in one go
        
        # Helper function to check if it's possible to eat all bananas with the given speed within h hours
        def is_feasible(max_speed):
            # Calculate the total hours required to eat all piles with the current speed
            # Each pile x takes math.ceil(x / max_speed) hours to finish
            return sum(math.ceil(x / max_speed) for x in piles) <= h

        # Set the initial search boundaries for binary search
        low, high = 1, 1000000000  # Low: at least 1 banana/hour, High: an arbitrarily large max speed
        
        # Perform binary search to find the minimum feasible eating speed
        while low <= high:
            mid = low + (high - low) // 2  # Calculate the midpoint (possible eating speed)
            
            # If the current speed `mid` can finish all piles in h or fewer hours, it's feasible
            if is_feasible(mid):
                high = mid - 1  # Try to find a smaller (more optimal) speed
            else:
                low = mid + 1  # If not feasible, increase the speed to reduce the total hours

        # After binary search finishes, `low` will be the smallest feasible eating speed
        return low
