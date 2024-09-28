class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the list
        
        # If there's only one element, it is the peak
        if n == 1:
            return 0
        
        # Check if the first element is a peak
        if nums[0] > nums[1]:
            return 0
        
        # Check if the last element is a peak
        if nums[-1] > nums[n - 2]:
            return n - 1
        
        # Initialize binary search boundaries, ignoring the first and last element
        lo, hi = 1, n - 2
        
        # Perform binary search within the range
        while lo <= hi:
            mid = lo + (hi - lo) // 2  # Calculate the middle index
            
            # Check if mid is a peak by comparing with its neighbors
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid  # If nums[mid] is greater than both neighbors, return it as the peak
            
            # If nums[mid] is smaller than its left neighbor, move to the left half
            elif nums[mid] < nums[mid - 1]:
                hi = mid - 1  # Narrow the search space to the left side
            
            # If nums[mid] is smaller than its right neighbor, move to the right half
            else:
                lo = mid + 1  # Narrow the search space to the right side
        
        # Given the problem's constraints, a peak element will always be found within the loop
        return lo
