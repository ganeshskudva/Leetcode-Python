# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the linked list by alternating nodes from the front and the back.
        Do not return anything, modifies the linked list in-place.
        """

        # Base case: if the list is empty, do nothing
        if not head:
            return 

        # Step 1: Use the fast-slow pointer technique to find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list starting from slow.next
        prev, curr = None, slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Disconnect the first half from the second
        slow.next = None
        
        # Step 3: Merge the two halves
        h1, h2 = head, prev
        while h2:
            # Store next pointers
            nxt1, nxt2 = h1.next, h2.next
            
            # Link alternating nodes from h1 and h2
            h1.next = h2
            h1 = nxt1
            
            h2.next = h1
            h2 = nxt2

# Time Complexity (TC):
# - Finding the middle of the list takes O(n), where n is the number of nodes.
# - Reversing the second half of the list also takes O(n/2) = O(n).
# - Merging the two halves takes O(n).
# - Thus, the total time complexity is O(n), where n is the length of the linked list.

# Space Complexity (SC):
# - The algorithm uses O(1) extra space because it only uses a few pointers (slow, fast, prev, curr, etc.).
# - The space complexity is O(1) since no additional data structures are used, and modifications are made in-place.
