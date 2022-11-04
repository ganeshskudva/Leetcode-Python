class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        i, j = 0, len(s) - 1
        tmp = list(s)

        while i <= j:
            if self.isVowel(tmp[i]) and self.isVowel(tmp[j]):
                tmp[i], tmp[j] = tmp[j], tmp[i]
                i, j = i + 1, j - 1
            else:
                if self.isValid(i, s) and not self.isVowel(tmp[i]):
                    i += 1
                if self.isValid(i, s) and not self.isVowel(tmp[j]):
                    j -= 1

        return ''.join(tmp)

    def isValid(self, idx, arr):
        return 0 <= idx < len(arr)

    def isVowel(self, ch):
        if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
            return True

        return False
