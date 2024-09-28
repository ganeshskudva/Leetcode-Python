class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Initialize the lower and upper bounds for binary search
        lo, hi = 1, num
        
        # Perform binary search to check if num is a perfect square
        while lo <= hi:
            # Calculate the middle value to check
            mid = lo + (hi - lo) // 2
            
            # Calculate the square of the mid value
            prod = mid * mid
            
            # If the square equals the target number, it is a perfect square
            if prod == num:
                return True
            # If the square is less than the target number, search the right half
            elif prod < num:
                lo = mid + 1
            # If the square is greater than the target number, search the left half
            else:
                hi = mid - 1
        
        # If no perfect square is found, return False
        return False
