class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Create a dictionary (mp) where each key is a character in `source`
        # and the value is a list of the indices where the character occurs in `source`.
        mp = defaultdict(list)
        for i, c in enumerate(source):
            mp[c].append(i)  # Append the index of the character `c` in `source`.

        # Binary search helper function to find the next valid position in `source`.
        # `arr` is the list of positions of the character in `source`, and `pos` is the current position.
        def bin_search(arr, pos):
            # If we are starting from the first character in source (pos == -1), return the first occurrence of the character.
            if pos == -1:
                return arr[0]
            # If `pos` is greater than or equal to the last position in `arr`, wrap around and return the first occurrence (circular).
            if pos >= arr[-1]:
                return arr[0]
            
            # Standard binary search to find the smallest index in `arr` that is greater than `pos`.
            lo, hi = 0, len(arr) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                # Narrow down the range based on comparison with `pos`.
                if arr[mid] > pos:
                    hi = mid  # Search the left half.
                else:
                    lo = mid + 1  # Search the right half.

            return arr[lo]  # Return the next valid position after `pos`.

        # `res` tracks how many times we need to go over `source`, initialized to 1 (at least one pass is needed).
        # `s_pos` keeps track of the current position in `source`.
        res, s_pos = 1, -1
        
        # Iterate over each character in the `target` string.
        for j in range(len(target)):
            ch_tgt = target[j]
            # If the character from `target` does not exist in `source`, it's impossible to form `target`.
            if ch_tgt not in mp:
                return -1

            # `pre` stores the previous position in `source`.
            pre = s_pos
            # Use binary search to find the next valid position for the current character in `target`.
            s_pos = bin_search(mp[ch_tgt], s_pos)
            
            # If the new position `s_pos` is less than or equal to `pre`, it means we had to start over in `source`.
            if pre >= s_pos:
                res += 1  # Increment the number of passes over `source`.

        # Return the total number of passes needed to form `target`.
        return res


# with Py bisect for binary search

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Create a dictionary where each character maps to a list of its indices in `source`
        char_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)
        
        # Helper function to perform binary search to find the next valid position
        def find_next_position(indices, curr_pos):
            # Use `bisect_left` to find the smallest index greater than `curr_pos`
            idx = bisect_left(indices, curr_pos + 1)
            # If idx is out of bounds, we need to wrap around (start a new pass)
            if idx == len(indices):
                return indices[0]  # Start from the beginning of the source
            return indices[idx]

        # Initialize result counter (number of passes) and current position in `source`
        passes, curr_pos = 1, -1
        
        # Loop over each character in `target`
        for char in target:
            # If the character doesn't exist in `source`, return -1
            if char not in char_indices:
                return -1
            
            # Find the next position for the current character in `source`
            next_pos = find_next_position(char_indices[char], curr_pos)
            
            # If the next position is earlier in the `source`, this means we need another pass
            if next_pos <= curr_pos:
                passes += 1
                curr_pos = find_next_position(char_indices[char], -1)  # Start a new pass from the beginning
            else:
                curr_pos = next_pos  # Update current position to next_pos
        
        return passes
