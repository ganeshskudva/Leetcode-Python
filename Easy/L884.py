class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_cnt, s2_cnt = collections.Counter(s1.split(" ")), collections.Counter(s2.split(" "))
        res = []
        
        for k, v in s1_cnt.items():
            if v == 1 and k not in s2_cnt:
                res.append(k)
        
        for k, v in s2_cnt.items():
            if v == 1 and k not in s1_cnt:
                res.append(k)
            
        return res
        