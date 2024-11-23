class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to efficiently find subsequences
        n = len(nums)
        res = 0
        mod = 10**9 + 7  # Modulo to handle large numbers as required by the problem
        i, j = 0, n - 1  # Two pointers: i for the start and j for the end of the array
        
        # Iterate through the array with the two-pointer approach
        for i in range(n):
            # Adjust the right pointer `j` to find the maximum valid subsequence
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            
            # If a valid subsequence exists
            if i <= j and nums[i] + nums[j] <= target:
                # Add all possible subsequences that include nums[i] as the smallest element
                res += pow(2, (j - i), mod)  # 2^(j - i) subsequences
                res %= mod  # Ensure the result does not exceed the modulo
            
        return res

# Time Complexity (TC):
# O(n log n) - Sorting the array takes O(n log n), and the subsequent iteration with 
# two pointers takes O(n) in total. Thus, the dominant term is O(n log n).

# Space Complexity (SC):
# O(1) - No extra space is used except for a few variables; the sorting is in-place.
