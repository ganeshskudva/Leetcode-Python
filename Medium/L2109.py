class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []  # Result list to store the characters and spaces
        j = 0  # Pointer for the spaces list
        
        # Iterate through the string `s` with index and character
        for i, c in enumerate(s):
            # If the current index matches the next space index, add a space
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1  # Move to the next space index
            ans.append(c)  # Add the current character to the result
        
        # Join the result list into a single string and return
        return ''.join(ans)

# Time Complexity (TC): O(n)
# - Iterating through the string `s` takes O(n), where `n` is the length of `s`.
# - Checking the condition `j < len(spaces)` and `i == spaces[j]` for each character is O(1) per iteration.
# - Appending to the list `ans` and joining it into a string are O(n) operations in total.
# - The overall time complexity is O(n), as the processing for each character and space index is linear.

# Space Complexity (SC): O(n)
# - The list `ans` stores the result, which grows to the size of the final string, O(n).
# - The `spaces` list and the input string `s` are provided as input and do not contribute additional space complexity.
# - The final string constructed by `''.join(ans)` also requires O(n) space.
# - Overall, the space complexity is O(n).
