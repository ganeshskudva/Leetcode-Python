class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize the result array 'ret' with [-1, -1], representing the target is not found.
        ret = [-1, -1]
        
        # If the input list 'nums' is empty, return [-1, -1] as the target cannot be found.
        if not nums:
            return ret

        # Helper function that performs a binary search to find either the first or last occurrence of the target.
        def bs(start, first):
            lo, hi, res = start, len(nums) - 1, -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1  # Search the right half
                elif nums[mid] > target:
                    hi = mid - 1  # Search the left half
                else:
                    res = mid  # Target found, update result
                    if first:
                        hi = mid - 1  # Search left for the first occurrence
                    else:
                        lo = mid + 1  # Search right for the last occurrence
            return res

        # Find the first occurrence of the target.
        ret[0] = bs(0, True)
        
        # If the target is not found, return [-1, -1].
        if ret[0] == -1:
            return ret

        # Find the last occurrence of the target.
        ret[1] = bs(0, False)

        # Return the range [first occurrence, last occurrence].
        return ret

# Time Complexity (TC):
# 1. Binary search (bs) is called twice: once to find the first occurrence and once to find the last occurrence.
#    Each binary search runs in O(log(n)), where n is the length of the input array `nums`.
# 2. Therefore, the overall time complexity is O(2 * log(n)) = **O(log(n))**.

# Space Complexity (SC):
# 1. The algorithm uses O(1) additional space, as the binary search operates in-place without requiring extra data structures.
# 2. The `ret` array and a few integer variables (lo, hi, mid, res) are used, which are constant in size.
# 3. Therefore, the overall space complexity is **O(1)**.
