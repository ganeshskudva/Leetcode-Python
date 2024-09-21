class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers for binary search
        lo, hi = 0, len(nums) - 1
        
        # Perform binary search until `lo` meets `hi`
        while lo < hi:
            # Calculate the middle index
            mid = lo + (hi - lo) // 2
            
            # Check if `mid` is an even index
            if mid % 2 == 0:
                # If `nums[mid]` is equal to `nums[mid + 1]`, 
                # the single element must be on the right side, so we adjust `lo`.
                if nums[mid] == nums[mid + 1]:
                    lo = mid + 2  # Move past the paired element to the right side
                else:
                    # Otherwise, the single element is on the left side or at `mid`
                    hi = mid
            else:
                # If `mid` is odd, check if `nums[mid]` is equal to the previous element (`nums[mid - 1]`)
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1  # Single element must be on the right side
                else:
                    hi = mid  # Otherwise, it's on the left side
            
        # After the binary search, `lo` will point to the single non-duplicate element
        return nums[lo]
