class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Step 1: Initialize a boolean array to mark bold positions
        bold = [False] * len(s)
        
        # Step 2: Mark positions that need to be bolded
        for word in words:
            start = s.find(word)
            # Loop to find all occurrences of `word` in `s`
            while start != -1:
                # Mark all indices within the matched word as bold
                for i in range(start, start + len(word)):
                    bold[i] = True
                # Continue finding the word from the next position
                start = s.find(word, start + 1)
        
        # Step 3: Build the result string with <b> tags around bolded sections
        res = []
        i = 0
        while i < len(s):
            if bold[i]:
                # Start a bold tag
                res.append('<b>')
                # Append all contiguous bolded characters
                while i < len(s) and bold[i]:
                    res.append(s[i])
                    i += 1
                # Close the bold tag
                res.append('</b>')
            else:
                # Append non-bold character
                res.append(s[i])
                i += 1
        
        # Join all parts and return the final result string
        return ''.join(res)

# Time Complexity (TC):
# - Finding and marking bold indices: O(N * M), where N is the length of `s` and M is the number of words in `words`.
#   For each word in `words`, we search for all occurrences in `s`, which can take O(N) in the worst case.
# - Building the result string: O(N), where N is the length of `s`, as we iterate through `s` once.
# - Overall: O(N * M + N) = O(N * M), dominated by the marking phase.

# Space Complexity (SC):
# - Bold array: O(N), where N is the length of `s`, to store the boolean array marking bold indices.
# - Result list: O(N), where N is the length of `s`, to store the result string characters before joining.
# - Overall: O(N), as both the bold array and the result list are O(N).


# Heap based solution
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Step 1: Find intervals for each word in `words` within the string `s`
        intervals = []
        for w in words:
            start = s.find(w)
            # Loop to find all occurrences of `w` in `s`
            while start != -1:
                # Append start and end of each occurrence as an interval
                intervals.append((start, start + len(w)))
                # Move `start` forward by 1 to find overlapping occurrences
                start = s.find(w, start + 1)

        # Step 2: Merge overlapping intervals
        def merge():
            # Initialize a result list to store merged intervals
            ret = []
            # Transform intervals list into a min-heap
            heapify(intervals)

            # Merge intervals from the heap
            while intervals:
                st, end = heappop(intervals)
                # Merge overlapping intervals by extending the `end` as needed
                while intervals and end >= intervals[0][0]:  # Check overlap or adjacency
                    end = max(end, intervals[0][1])
                    heappop(intervals)
                # Append merged interval
                ret.append((st, end))

            return ret

        # Get merged intervals
        merged_intervals = merge()

        # Step 3: Build the final result string with <b> tags
        res, prev = [], 0
        for intvr in merged_intervals:
            # Add non-bolded text before the interval
            res.append(s[prev : intvr[0]])
            # Wrap bolded text for the interval
            res.append('<b>')
            res.append(s[intvr[0]: intvr[1]])
            res.append('</b>')
            # Update `prev` to end of the current interval
            prev = intvr[1]
        
        # Add any remaining text after the last interval
        if prev < len(s):
            res.append(s[prev:])
        
        # Join all parts and return the result string
        return ''.join(res)

# Time Complexity (TC):
# - Finding intervals: O(N * M), where N is the length of `s` and M is the number of words in `words`,
#   as `s.find(w)` is called repeatedly.
# - Merging intervals: O(K log K), where K is the number of intervals, due to heap operations.
# - Building the result string: O(N), where N is the length of `s`.
# - Overall: O(N * M + K log K + N), dominated by O(N * M + K log K).

# Space Complexity (SC):
# - Storage for intervals: O(K), where K is the number of intervals.
# - Storage for merged intervals: O(K).
# - Storage for result string: O(N), where N is the length of `s`.
# - Overall: O(K + N).

