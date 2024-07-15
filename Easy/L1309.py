class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []

        def get_char(val):
            return chr(ord('a') + val)

        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # Process two-digit number followed by '#'
                res.append(get_char(int(s[i:i + 2]) - 1))
                i += 3
            else:
                # Process single-digit number
                res.append(get_char(int(s[i]) - 1))
                i += 1

        return ''.join(res)
