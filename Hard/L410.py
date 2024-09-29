class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # If the input array is empty or k is zero, just return k.
        # This handles edge cases where the input is invalid.
        if not nums or not k:
            return k

        # Helper function to check if we can split the array into 'k' or fewer subarrays
        # such that the maximum sum of any subarray does not exceed 'capacity'.
        def is_valid(capacity):
            # 'cnt' is the number of subarrays formed so far, start with one subarray.
            # 'total' keeps track of the current subarray sum.
            cnt, total = 1, 0

            # Iterate over each element in the nums array.
            for n in nums:
                # Add the current number 'n' to the current subarray total.
                total += n

                # If adding 'n' causes the total to exceed 'capacity', we need to form a new subarray.
                if total > capacity:
                    # Reset 'total' to the current element 'n', which starts the new subarray.
                    total = n

                    # Increment the subarray count, as we have created a new subarray.
                    cnt += 1

            # If the number of subarrays we formed is less than or equal to 'k', return True.
            # This means the current 'capacity' is valid for splitting the array into 'k' or fewer subarrays.
            return cnt <= k

        # Initialize the binary search range:
        # 'lo' starts at the maximum value in the array (minimum valid subarray sum),
        # 'hi' starts at the sum of the entire array (maximum possible subarray sum).
        lo, hi = max(nums), sum(nums)

        # Perform binary search to find the smallest valid 'capacity' that allows us to split the array into 'k' subarrays.
        while lo <= hi:
            # Calculate the midpoint (potential 'capacity').
            mid = lo + (hi - lo) // 2

            # If 'mid' is a valid capacity (i.e., we can split the array into 'k' or fewer subarrays),
            # we attempt to find a smaller valid capacity by moving the upper bound down ('hi = mid - 1').
            if is_valid(mid):
                hi = mid - 1
            # If 'mid' is not a valid capacity (i.e., we need more than 'k' subarrays),
            # we need a larger capacity, so we move the lower bound up ('lo = mid + 1').
            else:
                lo = mid + 1

        # After the binary search, 'lo' will be the smallest valid capacity.
        return lo
