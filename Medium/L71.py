class Solution:
    def simplifyPath(self, path: str) -> str:
        res, st = [], []
        
        for s in path.split("/"):
            if s == '..':
                if st:
                    st.pop()
            elif s != "" and s != '.':
                st.append(s)
        
        if not st:
            return "/"
        
        for c in st:
            res.append('/')
            res.append(c)
                
        return ''.join(res)
