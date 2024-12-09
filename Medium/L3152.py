from typing import List

def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    # Compute the prefix sum array that tracks consecutive pairs with the same parity
    ps = [0]
    for i in range(1, len(nums)):
        ps.append(ps[-1] + (nums[i - 1] % 2 == nums[i] % 2))
    
    # Evaluate each query and check if the prefix sums are equal
    return [ps[q[0]] == ps[q[1]] for q in queries]

# Time Complexity (TC):
# 1. Computing the prefix sum array:
#    - This involves a single traversal of the input array `nums` of size `n`.
#    - Time Complexity: O(n), where `n` is the size of `nums`.
# 2. Processing the queries:
#    - Each query involves a single comparison of two prefix sum values, which is O(1).
#    - For `q` queries, the total cost is O(q).
# Overall Time Complexity: O(n + q), where `n` is the size of `nums` and `q` is the number of queries.

# Space Complexity (SC):
# 1. Storage for the prefix sum array `ps`:
#    - This array is of size `n`, corresponding to the size of `nums`.
#    - Space Complexity: O(n).
# 2. Storage for the result list:
#    - The result list contains `q` boolean values, one for each query.
#    - Space Complexity: O(q).
# Overall Space Complexity: O(n + q), where `n` is the size of `nums` and `q` is the number of queries.
