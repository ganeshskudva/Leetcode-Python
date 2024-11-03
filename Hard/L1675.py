import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # If nums is empty, return an infinitely large deviation as there are no numbers to compare
        if not nums:
            return float('inf')
        
        # Initialize a max-heap (by pushing negative values) to keep track of even numbers
        evens = []
        min_val = float('inf')  # Track the minimum value in the current state

        # Step 1: Normalize numbers by converting all numbers to even
        # - Push even numbers as is (negated for max-heap behavior)
        # - Double odd numbers to make them even, then push
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(evens, -num)  # Push even numbers
                min_val = min(num, min_val)
            else:
                heapq.heappush(evens, -num * 2)  # Make odd numbers even and push
                min_val = min(num * 2, min_val)

        # Initialize the result as infinity
        res = float('inf')

        # Step 2: Reduce deviation by reducing the maximum even number in the heap
        while evens[0] % 2 == 0:  # Continue while the largest number is even
            max_val = -heapq.heappop(evens)  # Get the current max even number
            res = min(res, max_val - min_val)  # Update the minimum deviation
            new_num = max_val // 2  # Divide the max even number by 2

            heapq.heappush(evens, -new_num)  # Push the new number back as negative
            min_val = min(new_num, min_val)  # Update min_val to the minimum of current min and new_num

        # Final check after the loop for when the max number becomes odd
        res = min(-evens[0] - min_val, res)
        return res

# Overall Time Complexity: O(n log m), where `n` is the number of elements in nums and `m` is the max number of times an even number can be divided by 2.
# Overall Space Complexity: O(n), for storing elements in the heap.
