class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()

        for e in emails:
            local, domain = e.split("@")
            tmp = []
            for ch in local:
                if ch == '.':
                    continue
                if ch == '+':
                    break
                tmp.append(ch)
            st.add(''.join(tmp) + '@' + domain)

        return len(st)
