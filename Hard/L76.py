class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If string `t` is longer than `s`, it's impossible to find a valid window, so return empty string
        if len(t) > len(s): 
            return ""

        # Use collections.Counter to create a frequency map of characters in string `t`
        mp = collections.Counter(t)
        
        # Initialize pointers for the sliding window (begin and end), 
        # 'head' will store the starting index of the minimum window.
        begin = end = head = 0
        # 'cnt' keeps track of how many unique characters in `t` still need to be matched in the current window.
        # 'length' keeps track of the size of the smallest window found (initialized to infinity).
        cnt, length = len(mp), float('inf')

        # Expand the window by moving `end` pointer
        while end < len(s):
            if s[end] in mp:  # If the current character is in `t`
                mp[s[end]] -= 1  # Decrease its count in the frequency map
                if mp[s[end]] == 0:  # If a character's count becomes 0, it means we have matched all instances of it
                    cnt -= 1  # Decrease `cnt`, indicating we have one less unique character to match
            end += 1  # Move the end pointer forward

            # Once we have matched all characters in `t` (i.e., cnt == 0)
            while cnt == 0:
                # Try to shrink the window by moving the `begin` pointer to the right
                if s[begin] in mp:  # If the character at `begin` is part of `t`
                    mp[s[begin]] += 1  # Increase its count in the frequency map
                    if mp[s[begin]] > 0:  # If the count becomes positive, we have removed one matching character
                        cnt += 1  # Increase `cnt` as we now need to find one more of this character

                # Update the minimum window if the current window is smaller
                if end - begin < length:
                    length, head = end - begin, begin  # Update the length and the start index of the minimum window
                begin += 1  # Move the begin pointer to shrink the window

        # If no valid window is found, return empty string. Otherwise, return the smallest valid window.
        return "" if length == float('inf') else s[head: head + length]
