from collections import Counter

class Solution:
    def numIdenticalPairs(self, A):
        # Count occurrences of each element in the list A
        counts = Counter(A)
        
        # Sum the number of good pairs for each unique element's count using the formula k * (k - 1) // 2
        # This calculates the number of ways to pick 2 indices (i, j) where i < j and A[i] == A[j]
        return sum(k * (k - 1) // 2 for k in counts.values())

# Space Complexity (SC): O(U)
# - The space complexity is O(U) where U is the number of unique elements in A.
# - This is because Counter(A) stores a count for each unique element in A.

# Time Complexity (TC): O(N)
# - The time complexity is O(N) for constructing the Counter, as we need to traverse the list A once to count occurrences.
# - Calculating the number of pairs involves iterating over the unique counts, which is O(U).
# - Since U ≤ N, the overall time complexity remains O(N).
