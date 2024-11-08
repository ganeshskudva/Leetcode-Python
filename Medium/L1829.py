from functools import reduce
from operator import ixor
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the maximum possible XOR value with 'maximumBit' bits, which will be (2^maximumBit - 1)
        # For example, if maximumBit = 3, maxXOR = 7 (binary: 111).
        maxXOR = (1 << maximumBit) - 1

        # Calculate the XOR of all elements in the list `nums`.
        # This will be the initial XOR of the entire array.
        arrayXOR = reduce(ixor, nums)
        
        # Initialize an empty list to store the results.
        ans = []

        # Iterate from the last element to the first (reverse order).
        for i in range(len(nums) - 1, -1, -1):
            # Calculate the maximum XOR possible with maxXOR by XORing it with arrayXOR.
            # This is the value that will be added to the result list.
            ans.append(arrayXOR ^ maxXOR)
            
            # Update arrayXOR by removing the contribution of the current element.
            # This simulates the effect of removing `nums[i]` from the array XOR.
            arrayXOR ^= nums[i]

        # Return the final list of answers.
        return ans
