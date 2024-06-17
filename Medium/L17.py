class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not digits:
            return ans

        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def solve(idx, tmp=[]):
            if idx > len(digits):
                return

            if len(tmp) == len(digits):
                ans.append(''.join(tmp))
                return

            curr_dig = digits[idx]
            for letter in mp[curr_dig]:
                tmp.append(letter)
                solve(idx + 1, tmp)
                del tmp[-1]

        solve(0)
        return ans
