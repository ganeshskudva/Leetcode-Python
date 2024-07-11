class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[i]
            
            if first_start <= second_end and second_start <= first_end:
                res.append([max(first_start, second_start), min(first_end, second_end)])
            
            if first_start <= second_end and second_start <= first_end:
                i += 1
            else :
                j += 1
        
        return res
