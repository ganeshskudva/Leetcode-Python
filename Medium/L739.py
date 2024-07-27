class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret, n = [0] * len(temperatures), len(temperatures)
        st = deque()
        
        for i in range(n - 1, -1, -1):
            cur = temperatures[i]
            while st and cur >= temperatures[st[-1]]:
                st.pop()
            if st:
                ret[i] = st[-1] - i
            st.append(i)
            
        return ret
