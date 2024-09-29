class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initialize two pointers: 'left' at the start of the array and 'right' at the end.
        left, right = 0, len(nums) - 1
        
        # Perform a binary search while 'left' is less than or equal to 'right'.
        while left <= right:
            # Calculate the middle index.
            mid = (left + right) // 2
            
            # If the target is found at the middle index, return True.
            if nums[mid] == target:
                return True
            
            # If the left half is sorted (nums[left] < nums[mid]).
            if nums[left] < nums[mid]:
                # Check if the target is within the sorted left half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow the search to the left half.
                else:
                    left = mid + 1  # Otherwise, search the right half.
            # If the right half is sorted (nums[left] > nums[mid]), meaning rotation occurred.
            elif nums[left] > nums[mid]:
                # Check if the target is within the sorted right half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Narrow the search to the right half.
                else:
                    right = mid - 1  # Otherwise, search the left half.
            else:
                # If nums[left] == nums[mid], we cannot determine which half is sorted,
                # so increment 'left' to move past duplicates and continue the search.
                left += 1
        
        # If the target is not found after the binary search, return False.
        return False
