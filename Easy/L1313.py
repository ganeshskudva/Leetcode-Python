class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # Initialize an empty result list and index pointer
        res, idx = [], 0
        
        # Loop through the nums list two elements at a time (freq and val pairs)
        while idx < len(nums):
            freq, val = nums[idx], nums[idx + 1]  # Extract frequency and value
            idx += 2  # Move to the next pair
            
            # Append 'val' to the result list 'freq' number of times
            for _ in range(freq):
                res.append(val)
        
        # Return the decompressed result list
        return res

# Time Complexity (TC):
# - The while loop runs len(nums) // 2 times (since we process two elements at a time).
# - Inside the loop, we append 'val' to the result list 'freq' times, making the total number of operations equal to the sum of all frequencies in the nums list.
# - Hence, the overall time complexity is O(n), where n is the total number of elements in the final decompressed list.

# Space Complexity (SC):
# - We are using an additional list 'res' to store the decompressed elements.
# - The space required is proportional to the total number of elements in the decompressed list, which is O(n), where n is the size of the final decompressed list.
