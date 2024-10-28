import random

class Solution:
    def findKthLargest(self, nums, k):
        # Edge case: if nums is empty, return None
        if not nums:
            return
        
        # Select a random pivot from the list
        pivot = random.choice(nums)
        
        # Partition the list into three parts:
        # - `left`: elements greater than the pivot
        # - `mid`: elements equal to the pivot
        # - `right`: elements less than the pivot
        left = [x for x in nums if x > pivot]
        mid  = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        # Calculate the lengths of `left` and `mid` partitions
        L, M = len(left), len(mid)
        
        # Determine where the k-th largest element lies based on the lengths of partitions
        if k <= L:
            # If k is within the range of elements in `left`, recurse into `left`
            return self.findKthLargest(left, k)
        elif k > L + M:
            # If k is greater than the combined length of `left` and `mid`, recurse into `right`
            # with adjusted k (excluding `left` and `mid` counts)
            return self.findKthLargest(right, k - L - M)
        else:
            # If k falls within the range of `mid`, return any element from `mid` as they are all equal
            return mid[0]

# Time Complexity (TC):
# - Average Case: O(n), where n is the number of elements in `nums`.
#   - Each recursive call approximately halves the input, leading to an average time complexity of O(n).
# - Worst Case: O(n^2), which occurs if partitioning is extremely unbalanced (rare with random pivot selection).

# Space Complexity (SC): O(n)
# - Each recursive call creates new partitions (`left`, `mid`, and `right`), each of which can take up to O(n) space.
# - In total, the space complexity is O(n) due to creating new lists in each recursive call.
