class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = [0] * 2051
        
        for birth, death in logs:
            year[birth] += 1
            year[death] -= 1
        
        max_num, max_year = year[1950], 1950
        
        for i in range(1951, len(year)):
            year[i] += year[i - 1]
            
            if year[i] > max_num:
                max_num = year[i]
                max_year = i
        
        return max_year
        
