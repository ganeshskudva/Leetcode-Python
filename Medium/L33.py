class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1  # If the list is empty, return -1

        # Helper function to find the index of the smallest element, i.e., the number of rotations in the array
        def rotation_cnt():
            lo, hi = 0, len(nums) - 1

            # Binary search to find the index where the array is rotated
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] > nums[hi]:
                    # If the middle element is greater than the last element, the smallest element is on the right
                    lo = mid + 1
                else:
                    # Otherwise, it is on the left (including mid)
                    hi = mid

            return lo  # Return the index of the smallest element (rotation count)

        rot_cnt = rotation_cnt()  # Get the rotation count
        low, high = 0, len(nums) - 1

        # Standard binary search with adjusted indices to account for the rotation
        while low <= high:
            mid = low + (high - low) // 2
            real_mid = (mid + rot_cnt) % len(nums)  # Adjust the middle index based on rotation

            if nums[real_mid] == target:
                return real_mid  # Target found, return its index
            elif nums[real_mid] < target:
                low = mid + 1  # Continue searching in the right half
            else:
                high = mid - 1  # Continue searching in the left half

        return -1  # If the target is not found, return -1

# Time Complexity (TC):
# - The rotation_cnt() function performs a binary search to find the rotation index. This takes O(log N) time.
# - The modified binary search (after finding the rotation index) also takes O(log N) time.
# - Therefore, the total time complexity is O(log N) + O(log N) = O(log N), where N is the length of the array.

# Space Complexity (SC):
# - The space complexity is O(1) because we are only using a few extra variables (lo, hi, mid, rot_cnt) for binary search,
#   and there is no additional data structure or recursion stack.
# - Thus, the space complexity is constant: O(1).
