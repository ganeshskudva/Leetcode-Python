class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, n, dict = 0, len(s), defaultdict(int)
        max_cnt, max_size = 0, 0

        def get_key(ch):
            return ord(ch) - ord('A')

        for end in range(n):
            dict[get_key(s[end])] += 1
            max_cnt = max(max_cnt, dict[get_key(s[end])])

            if end - start + 1 - max_cnt > k:
                dict[get_key(s[start])] -= 1
                start += 1

            max_size = max(max_size, end - start + 1)

        return max_size
