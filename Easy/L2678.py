class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 if int(d[-4:-2]) > 60 else 0 for d in details])
