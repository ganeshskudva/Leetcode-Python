class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, i = [], 0
        
        for p in pushed:
            st.append(p)
            while st and st[-1] == popped[i]:
                st.pop()
                i += 1
        
        return not st
        
