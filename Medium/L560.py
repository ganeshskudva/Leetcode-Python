class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize total sum and result counter
        tot = res = 0
        # Dictionary to store the frequency of cumulative sums
        mp = defaultdict(int)
        mp[0] = 1  # Base case for subarrays that start from the beginning

        # Iterate through each element in the list
        for n in nums:
            tot += n  # Update cumulative sum
            # If tot - k exists in mp, it means there is a subarray that sums to k
            res += mp[tot - k]  
            # Update the frequency of the current cumulative sum
            mp[tot] += 1

        return res  # Return the count of subarrays that sum to k

# Time Complexity (TC): O(n), where n is the length of the input list `nums`, since we iterate through `nums` once.
# Space Complexity (SC): O(n), for storing cumulative sums in the dictionary `mp`.
