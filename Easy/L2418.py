class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = sorted(zip(heights, names), reverse=True)

        return [n for _, n in lst]
