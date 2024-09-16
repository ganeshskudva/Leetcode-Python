class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # If k is zero or less, there are no valid subarrays, so return 0.
        if not k:
            return k
        
        # Initialize variables:
        # i: the left pointer of the sliding window.
        # n: the length of the input array nums.
        # prod: the current product of elements in the sliding window.
        # res: the result to store the count of subarrays with product less than k.
        i, n, prod, res = 0, len(nums), 1, 0
        
        # Iterate over the array using j as the right pointer of the sliding window.
        for j in range(n):
            # Multiply the current element nums[j] to the product.
            prod *= nums[j]
            
            # If the current product is greater than or equal to k, move the left pointer i to reduce the product.
            while i <= j and prod >= k:
                # Divide the product by nums[i] to remove the element at i from the window.
                prod //= nums[i]
                # Move the left pointer i to the right.
                i += 1
            
            # After adjusting the window, all subarrays ending at j and starting from i to j are valid.
            # The number of such subarrays is (j - i + 1).
            res += j - i + 1
        
        # Return the total count of subarrays with product less than k.
        return res