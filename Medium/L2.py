# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node to simplify operations on the result list
        self.head = ListNode(-1)
        res = self.head

        # Recursive function to process the addition of two numbers
        def solve(l1, l2, carry=0):
            # Base case: If both linked lists and carry are empty, we stop
            if not l1 and not l2 and not carry:
                return

            # Calculate the total sum of the current digits and carry
            tot = carry
            if l1:  # Add the value from the first list if it exists
                tot += l1.val
            if l2:  # Add the value from the second list if it exists
                tot += l2.val

            # Calculate new carry and current digit (val)
            carry, val = divmod(tot, 10)

            # Create a new node with the digit and append it to the result list
            self.head.next = ListNode(val)
            self.head = self.head.next  # Move to the next node

            # Recursively process the next nodes in l1, l2, and carry
            return solve(l1.next if l1 else None, l2.next if l2 else None, carry)

        # Start the recursive addition with the two lists
        solve(l1, l2)

        # Return the result list, starting from the next of the dummy node
        return res.next

# Time Complexity (TC):
# - The recursive function processes both linked lists node by node.
# - Since we traverse both linked lists exactly once, the time complexity is O(max(N, M)), where:
#   - N is the number of nodes in l1.
#   - M is the number of nodes in l2.
# - The carry is handled within the same iteration, so no additional time is added.

# Space Complexity (SC):
# - The space complexity depends on the depth of the recursion, which is determined by the length of the longer linked list.
# - The recursion stack will have at most max(N, M) recursive calls.
# - Thus, the space complexity is O(max(N, M)) due to the recursion stack.
# - Additionally, the space for the result list also grows proportionally to max(N, M), but it is part of the output.
