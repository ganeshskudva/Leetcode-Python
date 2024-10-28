import random

## quick-select
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

## heap based solution
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap with the first k elements
        hp = nums[:k]
        heapq.heapify(hp)  # Create a min-heap in O(k) time

        # Iterate over the remaining elements in nums starting from index k
        for n in nums[k:]:
            # If the current element is larger than the smallest element in the heap (hp[0]),
            # it means we can replace it to keep the heap containing the k largest elements
            if n > hp[0]:
                heapq.heapreplace(hp, n)  # Pop the smallest and push the current element in one step

        # The root of the heap (hp[0]) is the k-th largest element
        return hp[0]

# Time Complexity (TC): O(n log k)
# - Building the initial heap takes O(k) time.
# - For the remaining (n - k) elements, each insertion and removal operation takes O(log k),
#   resulting in O((n - k) log k) which simplifies to O(n log k) overall.

# Space Complexity (SC): O(k)
# - The heap stores only the k largest elements, resulting in O(k) space complexity.


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use `heapq.nlargest` to find the k largest elements in `nums`
        # The function returns a sorted list of the k largest elements in descending order
        # We access the last element in this list (`[-1]`), which is the k-th largest
        return heapq.nlargest(k, nums)[-1]

# Time Complexity (TC): O(n log k), where n is the number of elements in `nums`.
# - The `heapq.nlargest` function internally maintains a min-heap of size k to track the k largest elements.
# - Building this heap takes O(n log k) time, as each element insertion/removal in the heap of size k takes O(log k).

# Space Complexity (SC): O(k)
# - The `heapq.nlargest` function maintains a heap of the k largest elements, so it requires O(k) space.
# - The space complexity is efficient for large n with small k values.
