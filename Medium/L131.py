class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def solve(start, path=[]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    solve(end + 1, path)
                    path.pop()
        
        result = []
        solve(0)
        return result
