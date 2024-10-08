from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # Step 1: Build a dictionary to collect all (timestamp, website) tuples for each user
        # TC: O(n), SC: O(n)
        # n is the number of entries in the `username`, `timestamp`, and `website` arrays.

        # 'user_map' stores each user's website visits as a list of (timestamp, website) tuples.
        user_map = defaultdict(list)
        for i in range(len(username)):
            # Append (timestamp, website) tuple for each user.
            user_map[username[i]].append((timestamp[i], website[i]))

        # Step 2: Create a dictionary to count occurrences of each 3-sequence pattern
        # TC: O(m), SC: O(m)
        # m is the number of unique 3-sequence patterns across all users.

        count = defaultdict(int)  # Store the frequency of each 3-sequence pattern.
        result = ""  # To store the most frequent 3-sequence pattern.

        # Step 3: Define a DFS (recursion) function to generate all possible 3-sequences for each user
        def dfs(visit_list, path=None, idx=0):
            """
            DFS helper to generate all 3-combinations of websites.
            :param visit_list: List of websites sorted by timestamp
            :param path: The current 3-sequence being built
            :param idx: Current index in the recursion
            """
            # Initialize the path if not provided
            if path is None:
                path = []
            
            # If we've formed a 3-sequence, process it
            if len(path) == 3:
                pattern = ' '.join(path)  # Join the 3 websites into a string
                if pattern not in visited_patterns:  # Ensure this pattern hasn't been counted for this user
                    visited_patterns.add(pattern)  # Mark the pattern as visited
                    count[pattern] += 1  # Increment its occurrence in the global count

                    # Update the result if:
                    # - It's the first valid pattern (`result == ""`), or
                    # - The current pattern occurs more frequently than the previous result, or
                    # - The current pattern is lexicographically smaller in case of a tie in frequency.
                    nonlocal result
                    if result == "" or count[pattern] > count[result] or (
                        count[pattern] == count[result] and pattern < result):
                        result = pattern
                return  # Return after processing a valid 3-sequence

            # Recursively explore the next websites for forming a 3-sequence
            for i in range(idx, len(visit_list)):
                # Continue building the path by adding the next website
                dfs(visit_list, path + [visit_list[i][1]], i + 1)

        # Step 4: For each user, process all visits and generate all 3-sequence patterns using DFS
        # TC: O(u * k^3) where u is the number of users and k is the number of websites visited by each user
        # SC: O(u * k^3) for recursion and storing unique patterns.
        for user, visits in user_map.items():
            # Sort the user's website visits by timestamp (first element in the tuple).
            visits.sort()  # TC: O(k log k) where k is the number of visits for the user
            
            # To avoid counting the same 3-sequence multiple times for one user, use a set.
            visited_patterns = set()

            # Start DFS for each user to explore all possible 3-sequence combinations.
            dfs(visits)

        # Step 5: Return the final result as a list of 3 websites (split the string by space).
        # TC: O(1), SC: O(1)
        return result.split()

# Time Complexity (TC):
# 1. Building the user_map takes O(n), where n is the total number of entries (size of `username`, `timestamp`, and `website`).
# 2. Sorting the visits for each user takes O(k log k), where k is the number of visits per user.
# 3. The DFS function explores all 3-sequence combinations for each user, which takes O(k^3) per user in the worst case (k choose 3).
# 4. Counting all 3-sequence patterns across all users takes O(u * k^3), where u is the number of users and k is the number of websites visited by each user.

# Space Complexity (SC):
# 1. Storing the user_map requires O(n) space for storing all user visits.
# 2. The count dictionary requires O(m) space, where m is the number of unique 3-sequences.
# 3. The visited_patterns set and recursion depth use O(k^3) space in the worst case for each user.
# Overall, the space complexity is O(n + m).