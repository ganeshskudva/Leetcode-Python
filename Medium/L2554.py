class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Convert the banned list to a set for O(1) lookup
        banned_set = set(banned)

        # Initialize total sum and count
        tot, cnt = 0, 0

        # Iterate through numbers from 1 to n, skipping banned numbers
        for i in range(1, n + 1):
            if i not in banned_set:  # Proceed only if the number is not banned
                if tot + i > maxSum:  # Stop early if adding the current number exceeds maxSum
                    break
                tot += i
                cnt += 1  # Increment the count for valid numbers

        return cnt

# Time Complexity (TC): 
# O(n) - Iterates over numbers from 1 to n. Membership checks in the set are O(1) on average.
# Space Complexity (SC): 
# O(b) - Space required to store the banned set, where b is the length of the banned list.
