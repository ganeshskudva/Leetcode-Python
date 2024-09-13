class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hash = {}
        res = []
        j = 0

        for c in key:
            if c == ' ':
                continue
            if c not in hash:
                hash[c] = chr(ord('a') + j)
                j += 1

        for c in message:
            if c == ' ':
                res.append(' ')
            else:
                res.append(hash[c])

        return ''.join(res)