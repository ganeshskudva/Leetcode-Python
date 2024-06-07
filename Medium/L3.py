class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, max_len, left, dict = len(s), 0, 0, defaultdict(int)

        for right in range(n):
            if s[right] in dict and dict[s[right]] >= left:
                left = dict[s[right]] + 1
            dict[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
