class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        This function finds the maximum number of vowels in any substring of size 'k' in the given string 's'.
        
        Parameters:
        s (str): The input string consisting of lowercase letters.
        k (int): The size of the substring to check for the maximum number of vowels.
        
        Returns:
        int: The maximum number of vowels in any substring of size 'k'.
        """

        # Define a set containing all the vowel characters for quick lookup.
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize sliding window variables:
        # 'left' is the starting index of the sliding window.
        # 'mx' stores the maximum number of vowels found in any window of size 'k'.
        # 'cnt' counts the number of vowels in the current window.
        left, mx, cnt = 0, float('-inf'), 0
        
        # Helper function to check if a character is a vowel.
        def is_vowel(ch):
            return ch in vowels

        # Iterate through the string with 'right' as the right boundary of the sliding window.
        for right in range(len(s)):
            
            # If the character at the 'right' pointer is a vowel, increment the vowel count.
            if is_vowel(s[right]):
                cnt += 1

            # Calculate the size of the current window.
            win_sz = right - left + 1
            
            # If the window size exceeds 'k', we need to shrink the window from the left.
            if win_sz > k:
                # If the character at the 'left' pointer is a vowel, decrement the vowel count.
                if is_vowel(s[left]):
                    cnt -= 1
                # Move the 'left' pointer to the right to shrink the window.
                left += 1
            
            # Update the maximum number of vowels found in any window of size 'k'.
            mx = max(mx, cnt)

        # Return the maximum number of vowels found in any window of size 'k'.
        return mx
