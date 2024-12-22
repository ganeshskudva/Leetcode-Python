from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(self, A, queries):
        n = len(A)
        qn = len(queries)
        
        # Initialize query buckets for each building
        que = defaultdict(list)
        res = [-1] * qn  # Initialize results array with -1
        
        # Step 1: Preprocess direct answers
        for qi, (i, j) in enumerate(queries):
            if i < j and A[i] < A[j]:  # Left to right increasing height
                res[qi] = j
            elif i > j and A[i] > A[j]:  # Right to left decreasing height
                res[qi] = i
            elif i == j:  # Same building, trivial case
                res[qi] = i
            else:
                # Step 2: Bucketize queries for deferred processing
                que[max(i, j)].append((max(A[i], A[j]), qi))
        
        # Step 3: Process buildings and answer deferred queries
        heap = []  # Min-heap to manage queries
        for i in range(n):
            # Resolve all queries where the current building satisfies conditions
            while heap and heap[0][0] < A[i]:
                _, qi = heappop(heap)
                res[qi] = i
            
            # Add queries targeting this building to the heap
            for q in que[i]:
                heappush(heap, q)
        
        return res

# Time Complexity (TC):
# - Initial loop to bucketize queries: O(qn), where qn is the number of queries.
# - Second loop processes all queries and buildings: O(n + qn * log(qn)), since heap operations are logarithmic.
# Overall: O(n + qn * log(qn)).

# Space Complexity (SC):
# - Storage for query buckets: O(qn).
# - Min-heap for processing queries: O(qn).
# - Result array: O(qn).
# Overall: O(qn + n).
