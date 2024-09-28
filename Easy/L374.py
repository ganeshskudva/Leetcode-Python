# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the low (lo) and high (hi) bounds for binary search
        lo, hi = 0, n
        
        # Continue the binary search until lo surpasses hi
        while lo <= hi:
            # Calculate the middle point to check using binary search formula
            mid = lo + (hi - lo) // 2
            
            # Call the guess API to check the mid value
            res = guess(mid)
            
            # If the result is 0, it means we found the correct number
            if res == 0:
                return mid
            
            # If the result is 1, the picked number is higher, so we search the right half
            elif res == 1:
                lo = mid + 1
            
            # If the result is -1, the picked number is lower, so we search the left half
            else:
                hi = mid - 1
        
        # If the loop finishes, return the low bound as the guessed number
        return lo
