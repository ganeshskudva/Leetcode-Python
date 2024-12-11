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

# Time Complexity (TC):
# 1. In the worst-case scenario, where duplicates are present, the algorithm may need to perform a linear scan.
#    - This happens when `nums[left] == nums[mid]`, and we increment `left` repeatedly.
#    - This results in O(n) time complexity in the worst case.
# 2. In the best-case scenario, when no duplicates are present, the binary search runs in O(log(n)).
# Overall: **O(n)** in the worst case, **O(log(n))** in the best case.

# Space Complexity (SC):
# 1. The algorithm uses O(1) extra space, as it only employs pointers (`left`, `right`, `mid`) and does not require additional data structures.
# Overall: **O(1)**.
