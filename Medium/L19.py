# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case: if the linked list is empty, return the head (None in this case)
        if not head:
            return head
        
        # Initialize two pointers, slow and fast, both starting at the head
        slow, fast = head, head
        
        # Move the 'fast' pointer 'n' nodes ahead of the 'slow' pointer
        for _ in range(n):
            fast = fast.next  # Move fast pointer forward by one
        
        # If 'fast' becomes None after moving 'n' steps, it means the node to be removed
        # is the head node itself. Return the second node as the new head.
        if not fast:
            return head.next
        
        # Move both 'slow' and 'fast' pointers one step at a time until 'fast' reaches the end
        # 'slow' will then point to the node just before the one to be removed
        while fast.next:
            slow, fast = slow.next, fast.next
        
        # Adjust the 'next' pointer of the 'slow' node to skip the target node
        slow.next = slow.next.next
        
        # Return the (possibly modified) head of the linked list
        return head
