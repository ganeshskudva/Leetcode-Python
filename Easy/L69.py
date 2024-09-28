class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize the lower and upper bounds for binary search
        lo, hi = 1, x

        # Perform binary search to find the square root
        while lo <= hi:
            # Calculate the middle value to check
            mid = lo + (hi - lo) // 2
            
            # Calculate the square of the mid value
            prod = mid * mid
            
            # If the square is less than x, the square root must be higher
            if prod < x:
                lo = mid + 1
            # If the square is greater than x, the square root must be lower
            elif prod > x:
                hi = mid - 1
            # If the square is exactly x, return mid as the square root
            else:
                return mid

        # If no exact square root is found, return the floor value, which is 'hi'
        return hi
