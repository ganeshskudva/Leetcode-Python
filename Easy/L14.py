class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1, s2, idx = strs[0], strs[-1], 0

        while idx < len(s1) and idx < len(s2):
            if s1[idx] == s2[idx]:
                idx += 1
            else:
                break

        return s1[:idx]
