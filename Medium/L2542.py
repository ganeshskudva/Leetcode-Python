import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, hp, res, tot = len(nums1), [], 0, 0  # Initialize variables
        
        # Combine nums1 and nums2 into pairs with nums2 values negated for sorting
        # We use -nums2 to get a descending order when sorted
        ess = [[-nums2[i], nums1[i]] for i in range(len(nums1))]
        
        # Sort the pairs by nums2 values in descending order
        # Time Complexity: O(n log n) due to sorting
        ess.sort()
        
        # Traverse each pair in sorted order
        for n2, n1 in ess:
            # Add the nums1 value to the min-heap and to the total sum
            # Time Complexity: O(log k) for each push operation
            heapq.heappush(hp, n1)
            tot += n1
            
            # If the heap size exceeds k, pop the smallest element to keep only the k largest elements
            if len(hp) > k:
                tot -= heapq.heappop(hp)  # Maintain only k elements in the heap
            
            # If we have exactly k elements, calculate the potential result
            if len(hp) == k:
                # Update the result to be the maximum of the current result and the new computed score
                res = max(res, tot * -n2)  # Multiply by -n2 to get the original nums2 value
        
        # Return the maximum score obtained
        return res

# Overall Time Complexity: O(n log n) due to sorting and O(n log k) for heap operations, making it O(n log n + n log k) in total.
# Overall Space Complexity: O(k) for storing elements in the heap.
