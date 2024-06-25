class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
                continue
            if ord(abbr[j]) <= ord('0') or ord(abbr[j]) > ord('9'):
                return False
            start = j
            while j < len(abbr) and ord('0') <= ord(abbr[j]) <= ord('9'):
                j += 1
            i += int(abbr[start: j + 1])

        return i == len(word) and j == len(abbr)
