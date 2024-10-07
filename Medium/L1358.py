class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize variables:
        # 'left' points to the start of the sliding window
        # 'cnt' keeps a count of each character ('a', 'b', 'c') within the window using defaultdict
        # 'res' stores the result (number of valid substrings)
        # 'n' is the length of the input string 's'
        left, cnt, res, n = 0, defaultdict(int), 0, len(s)

        # Iterate over the string with 'right' as the end of the sliding window
        for right in range(n):
            # Add the character at 'right' index to the 'cnt' dictionary
            cnt[s[right]] += 1

            # If we have at least one 'a', 'b', and 'c' in the current window, it's valid
            while cnt['a'] and cnt['b'] and cnt['c']:
                # Move 'left' forward to reduce the window and try to find the smallest valid window
                cnt[s[left]] -= 1
                left += 1
            
            # The number of valid substrings ending at 'right' is now increased by 'left'
            # because every substring between 'left' and 'right' that contains 'a', 'b', and 'c' is valid
            res += left

        # Return the total number of valid substrings
        return res
