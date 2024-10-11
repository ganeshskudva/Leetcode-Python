class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            # Base cases: if one of the lists is empty, return the other
            if not l1:
                return l2
            if not l2:
                return l1
            
            # Recursive merge: compare current values of l1 and l2, and link the smaller value to the result
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
        
        def partition(start, end):
            # Base case: if there's only one list, return it
            if start == end:
                return lists[start]
            
            # If the range is invalid, return None
            if start >= end:
                return None
            
            # Divide the range into two halves
            q = (start + end) // 2
            # Recursively merge the two halves
            l1 = partition(start, q)
            l2 = partition(q + 1, end)
            
            # Merge the two halves
            return merge(l1, l2)
        
        # Start merging from index 0 to len(lists) - 1
        return partition(0, len(lists) - 1)

# Time Complexity (TC):
# - The merge function merges two lists in O(m + n), where m and n are the lengths of the two lists.
# - The partition function divides the list range into two halves in a divide-and-conquer manner. The depth of recursion is log(k), where k is the number of lists.
# - At each level of recursion, every pair of lists is merged, and since the total number of elements across all lists is N, the overall time complexity is O(N log k), where N is the total number of nodes in all lists and k is the number of lists.

# Space Complexity (SC):
# - The space complexity is determined by the recursion depth, which is O(log k) due to the partitioning.
# - Additional space is used for recursive calls to the merge function, so the overall space complexity is O(log k), where k is the number of lists.
