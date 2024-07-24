class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mp, res = defaultdict(list), []
        for n in nums:
            n_str, tmp = str(n), []
            for ch in n_str:
                tmp.append(str(mapping[int(ch)]))
            mp[int(''.join(tmp))].append(n)

        for k in sorted(mp.keys()):
            res.extend(mp[k])

        return res
