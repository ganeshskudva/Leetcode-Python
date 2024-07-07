class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        mp = collections.Counter(t)
        begin = end = head = 0
        cnt, length = len(mp), float('inf')

        while end < len(s):
            if s[end] in mp:
                mp[s[end]] -= 1
                if not mp[s[end]]: 
                    cnt -= 1
            end += 1

            while not cnt:
                if s[begin] in mp:
                    mp[s[begin]] += 1
                    if mp[s[begin]] > 0: 
                        cnt += 1

                if end - begin < length:
                    length, head = end - begin, begin
                begin += 1

        return "" if length == float('inf') else s[head: head + length]
