class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        begin, end = 0, len(s) - 1
        while begin <= end:
            curr_first, curr_last = s[begin], s[end]
            if not( curr_first.isdigit() or curr_first.isalpha()):
                begin += 1
            elif not(curr_last.isdigit() or curr_last.isalpha()):
                end -= 1
            else:
                if curr_last.lower() != curr_first.lower():
                    return False
                begin, end = begin + 1, end - 1
        
        return True
