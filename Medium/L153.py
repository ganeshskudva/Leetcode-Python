class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize 'lo' to the start of the array and 'hi' to the end of the array.
        lo, hi, mid, n = 0, len(nums) - 1, 0, len(nums)
        
        # Binary search continues while 'lo' is less than 'hi'
        while lo < hi:
            # Calculate the middle index
            mid = lo + (hi - lo) // 2
            
            # If the middle element is less than the high element, it means the minimum
            # lies in the left half of the current range, including 'mid'.
            if nums[mid] < nums[hi]:
                # Narrow the search to the left half (including 'mid')
                hi = mid
            else:
                # If the middle element is greater than or equal to the high element,
                # it means the minimum is in the right half (excluding 'mid').
                # Move 'lo' to the next element after 'mid', using modulo to wrap around the array.
                lo = mid + 1
        
        # After the loop, 'lo' will point to the minimum element
        return nums[lo]
