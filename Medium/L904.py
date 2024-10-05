class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        This function solves the 'Fruit Into Baskets' problem. The goal is to 
        find the longest subarray where there are at most two distinct types of fruits.
        
        Parameters:
        fruits (List[int]): A list where each element represents a type of fruit.
        
        Returns:
        int: The maximum length of the subarray containing at most two distinct fruit types.
        """
        
        # Initialize a dictionary `cnt` to keep track of the count of each fruit type in the current window.
        cnt = defaultdict(int)
        
        # `left` is the starting index of the sliding window.
        left = 0
        
        # `max_len` will store the maximum length of a valid subarray (subarray with at most 2 distinct fruit types).
        max_len = float('-inf')  # Start with negative infinity, so any valid subarray will overwrite this value.

        # Iterate over the list `fruits` with `right` as the index for the sliding window's right boundary, and `v` as the fruit type.
        for right, v in enumerate(fruits):
            
            # Add the current fruit type (`v`) to the count dictionary `cnt`.
            cnt[v] += 1
            
            # If the window has more than 2 distinct types of fruits, shrink the window from the left.
            if len(cnt) > 2:
                
                # Decrease the count of the fruit at the left boundary.
                cnt[fruits[left]] -= 1
                
                # If the count of the fruit at the left boundary becomes zero, remove it from the dictionary.
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                
                # Move the left boundary of the window to the right, shrinking the window.
                left += 1
            
            # Update `max_len` with the maximum length of any valid subarray found so far.
            # A valid subarray contains at most 2 distinct types of fruits.
            max_len = max(max_len, right - left + 1)

        # Return the maximum length of any valid subarray found.
        return max_len
