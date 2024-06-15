class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            sorted_w = "".join(sorted(word))
            map[sorted_w].append(word)
        return list(map.values())
