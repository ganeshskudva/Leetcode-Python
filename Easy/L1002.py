class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        
        for i in range(1, len(words)):
            res &= collections.Counter(words[i])
        
        return list(res.elements())
