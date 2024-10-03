class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Step 1: Get the length of the array
        n = len(nums)

        # Step 2: Calculate the target, which is the sum of the array modulo p.
        # We want to find the smallest subarray whose sum makes the whole array divisible by p.
        target = sum(nums) % p

        # Step 3: If the sum of the array is already divisible by p, return 0
        # because no subarray needs to be removed.
        if not target:  # target == 0 means no remainder, sum is divisible by p
            return 0

        # Step 4: Initialize `answer` to `n` (the maximum possible size of the subarray).
        # We'll try to minimize this.
        answer = n

        # Step 5: Initialize `prefix_sum` to keep a running total of the prefix sums.
        # `hashmap` stores the prefix sum modulo p values, along with their index.
        # We initialize it with {0: -1} to handle cases where the prefix itself makes the array divisible by p.
        prefix_sum = 0
        hashmap = {0: -1}

        # Step 6: Iterate through the array to calculate prefix sums and find the subarray to remove.
        for i, num in enumerate(nums):
            # Update the running total (prefix sum)
            prefix_sum += num

            # Step 7: Calculate the key that we want to look for in the hashmap.
            # We're checking if there was a previous prefix sum that, when combined with the target,
            # results in a sum divisible by p.
            key = (prefix_sum % p - target) % p

            # Step 8: If this key exists in the hashmap, it means we've found a valid subarray.
            # We calculate the length of this subarray (i - hashmap[key]) and update the answer with the minimum value.
            if key in hashmap:
                answer = min(answer, i - hashmap[key])

            # Step 9: Update the hashmap with the current prefix sum modulo p and its index.
            hashmap[prefix_sum % p] = i

        # Step 10: If we found a subarray whose removal makes the sum divisible by p, return its size.
        # If not, return -1 (which means no valid subarray was found).
        return answer if answer < n else -1
