class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Find the number of subarrays with a sum divisible by k.

        Args:
        nums (List[int]): List of integers.
        k (int): The divisor.

        Returns:
        int: Count of subarrays with a sum divisible by k.

        Time Complexity: O(n), where n is the size of the input array.
            - We iterate through the array once, and dictionary operations (insert and lookup) are O(1) on average.
        
        Space Complexity: O(k), as the hash map stores at most k different remainders.
        """
        # Initialize variables
        count = 0
        total_sum = 0
        remainder_count = defaultdict(int)
        remainder_count[0] = 1  # To account for subarrays starting from the beginning

        for num in nums:
            # Update running sum and calculate remainder
            total_sum += num
            remainder = total_sum % k

            # Handle negative remainders to ensure they're in the range [0, k-1]
            if remainder < 0:
                remainder += k

            # Add the count of previous subarrays with the same remainder
            count += remainder_count[remainder]
            
            # Update the count of the current remainder in the hash map
            remainder_count[remainder] += 1

        return count

# Time Complexity: O(n), where n is the size of the input array.
# Space Complexity: O(k), as the hash map stores at most k different remainders.
