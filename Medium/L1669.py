class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # Step 1: Find the node just before the "a"th node in list1 (node_a)
        node_a = list1        
        for i in range(0, a - 1):
            node_a = node_a.next
            
        # Step 2: Find the node just after the "b"th node in list1 (node_b)
        node_b = list1
        for i in range(0, b + 1):
            node_b = node_b.next
            
        # Step 3: Find the last node of list2 (list2_tail)
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        
        # Step 4: Connect the end of list2 (list2_tail) to node_b
        node_a.next = list2  # Connect node_a to the head of list2
        list2_tail.next = node_b  # Connect the tail of list2 to node_b
        
        return list1  # Return the modified list1

# Time Complexity (TC):
# - Finding node_a requires O(a) time (traversing from the start of list1 to the (a-1)th node).
# - Finding node_b requires O(b) time (traversing from the start of list1 to the (b+1)th node).
# - Finding list2_tail requires O(len(list2)) time, where len(list2) is the length of list2.
# - Overall, the time complexity is O(a + b + len(list2)).

# Space Complexity (SC):
# - The space complexity is O(1) because we are only using a constant amount of extra space for the pointers (node_a, node_b, list2_tail).
# - No additional data structures are used, so the space complexity remains constant.
