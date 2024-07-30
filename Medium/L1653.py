class Solution:
    def minimumDeletions(self, s: str) -> int:
        st, res = [], 0
        
        for c in s:
            if st and st[-1] == 'b' and c == 'a':
                st.pop()
                res += 1
            else:
                st.append(c)
        return res
