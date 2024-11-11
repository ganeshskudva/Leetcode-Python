from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Sort the logs using a custom sort key defined by the `sort` function
        return sorted(logs, key=self.sort)

    def sort(self, log: str):
        # Split each log into two parts: identifier and the rest of the content
        identifier, content = log.split(' ', 1)
        
        # Check if the log content starts with a letter (indicating a letter log)
        if content[0].isalpha():
            # For letter logs, prioritize by content, then by identifier if contents are the same
            return (0, content, identifier)
        else:
            # For digit logs, prioritize by type, placing them after letter logs
            return (1, None, None)

# Time Complexity (TC): O(m * n log n)
# - n is the number of logs, and m is the maximum length of each log.
# - The sorting operation is O(n log n), and each comparison involves O(m) string operations for splitting and checking, making the overall complexity O(m * n log n).

# Space Complexity (SC): O(m * n)
# - We need space to store the sorted logs and intermediate splits.
# - In the worst case, this is O(m * n), where we have n logs, each of length m.
