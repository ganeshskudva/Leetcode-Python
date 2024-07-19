class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_st, max_st = set(), set()

        for row in matrix:
            min_st.add(min(row))
        for col in zip(*matrix):
            maxi = max(col)
            if maxi in min_st:
                max_st.add(maxi)
        
        return list(max_st)
