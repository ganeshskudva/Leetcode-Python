class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Hash map to store the first occurrence of each remainder when dividing running_sum by k
        # Initialized with {0: -1} to handle cases where a valid subarray starts at the beginning
        dict = defaultdict(int)
        dict[0] = -1
        
        # Variable to store the running sum of elements
        running_sum = 0

        # Iterate through the array
        for i in range(len(nums)):
            running_sum += nums[i]  # Update the running sum
            
            # Take modulo k to focus on remainders (only if k is non-zero)
            if k:
                running_sum %= k
            
            # Check if this remainder was seen before
            if running_sum in dict:
                # If the same remainder exists and the subarray length is at least 2, return True
                if i - dict[running_sum] > 1:
                    return True
            else:
                # Store the first occurrence of this remainder with its index
                dict[running_sum] = i

        # No valid subarray found
        return False

# Time Complexity (TC): O(n)
# - We traverse the nums array once, making the time complexity O(n).
# - Hash map operations (insertion and lookup) are O(1) on average.

# Space Complexity (SC): O(k)
# - In the worst case, the hash map can store up to k unique remainders (0 to k-1),
#   making the space complexity O(k). If k is very large or 0, it becomes O(n).
