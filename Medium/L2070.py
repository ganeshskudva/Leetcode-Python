from typing import List
from operator import itemgetter

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items based on the first element (price)
        items.sort()
        
        # Precompute the maximum beauty at each price point by taking the cumulative max beauty
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        
        # Define a closure to perform binary search on the sorted items
        def binary_search(target: int) -> int:
            lo, hi = 0, len(items) - 1
            while lo < hi:
                mid = (lo + hi + 1) >> 1  # Find the rightmost item
                if items[mid][0] > target:
                    hi = mid - 1
                else:
                    lo = mid
            return items[lo][1] if items[lo][0] <= target else 0

        # Apply binary search for each query
        result = [binary_search(query) for query in queries]
        
        return result

# Time Complexity:
# Sorting the items takes O(n log n), where n is the number of items.
# Each query uses binary search on items, which is O(log n), repeated for each query (q queries).
# Thus, the overall time complexity is O(n log n + q log n), where n is the number of items and q is the number of queries.

# Space Complexity:
# The additional space used is O(1) for the binary_search closure, ignoring the space required for the result array.
# Hence, the space complexity is O(1).