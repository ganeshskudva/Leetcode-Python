class Solution:
    def similarPairs(self, words: List[str]) -> int:
        lst = [sorted(set(w)) for w in words]
        mp = defaultdict(int)

        for l in lst:
            key = ''.join(l)
            mp[key] += 1

        return sum([v * (v - 1)//2 for _, v in mp.items()])
