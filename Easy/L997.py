class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Step 1: Handle the base case where there is only one person and no trust relationships.
        # If n == 1 and there are no trust pairs, that single person must be the judge.
        if not trust and n == 1:
            return n
        
        # Step 2: Create two arrays to track in-degrees and out-degrees for each person.
        # in_degree[i] counts how many people trust person i.
        # out_degree[i] counts how many people person i trusts.
        # We use size n+1 arrays to make the indexing straightforward (1-based).
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        # Step 3: Populate the in-degree and out-degree arrays.
        # For each pair (a, b) in trust:
        # - Person 'a' trusts person 'b', so increment out_degree[a] and in_degree[b].
        for a, b in trust:
            out_degree[a] += 1  # a trusts someone
            in_degree[b] += 1   # someone trusts b
        
        # Step 4: Find the judge by checking each person from 1 to n.
        # A judge must have an out-degree of 0 (doesn't trust anyone) and an in-degree of n-1 (trusted by everyone except themselves).
        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i  # This person is the judge.
        
        # Step 5: If no judge is found, return -1.
        return -1

# Time Complexity (TC):
# - Step 1 (initial check): Takes O(1) as it's just checking conditions.
# - Step 2 (array creation): Creating the in_degree and out_degree arrays takes O(n) since we're creating two arrays of size n+1.
# - Step 3 (trust list iteration): We iterate through the trust list, which contains m pairs. For each pair, we perform two constant-time operations (incrementing in_degree and out_degree). This step takes O(m) time, where m is the length of the trust list.
# - Step 4 (judge check): We loop through each person from 1 to n to check the judge conditions, which takes O(n).
# - Overall, the time complexity is O(n + m), where n is the number of people, and m is the number of trust relationships.

# Space Complexity (SC):
# - We use two arrays of size n+1 (in_degree and out_degree), each requiring O(n) space.
# - The trust list itself takes O(m) space, but this is part of the input, not additional space used by the algorithm.
# - Overall, the space complexity is O(n), where n is the number of people, since the two arrays dominate the space usage.
