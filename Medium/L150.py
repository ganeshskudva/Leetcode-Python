class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()

        for ch in tokens:
            if ch in ['+', '*']:
                v1, v2 = st.pop(), st.pop()
                if ch == '+':
                    st.append(v1 + v2)
                else:
                    st.append(v1 * v2)
            elif ch in ['-', '/']:
                v1, v2 = st.pop(), st.pop()
                if ch == '-':
                    st.append(v2 - v1)
                else:
                    st.append(int(v2/v1))
            else:
                st.append(int(ch))

        return st.pop()
