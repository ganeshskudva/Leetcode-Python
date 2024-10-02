class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp, srt, idx = {}, sorted(arr), 1
        
        for i in range(len(srt)):
            if srt[i] not in mp:
                mp[srt[i]] = idx
                idx += 1

        
        return [mp[n] for n in arr]