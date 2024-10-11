class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        maxVal = 0

        # Step 1: Find the middle of the linked list using slow and fast pointers
        while fast and fast.next:
            fast = fast.next.next  # Fast pointer moves two steps
            slow = slow.next       # Slow pointer moves one step

        # Step 2: Reverse the second half of the linked list
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next  # Reverse links

        # Step 3: Calculate the maximum twin sum by comparing values from
        # the first half (head) and the reversed second half (prev)
        while prev:
            maxVal = max(maxVal, head.val + prev.val)  # Compute pair sum
            prev = prev.next  # Move to the next node in the reversed second half
            head = head.next  # Move to the next node in the first half

        return maxVal  # Return the maximum pair sum

# Time Complexity (TC): O(n), where n is the number of nodes in the linked list.
# The list is traversed three times: 
# 1. Once to find the middle of the list (O(n/2)).
# 2. Once to reverse the second half of the list (O(n/2)).
# 3. Once to calculate the pair sums (O(n/2)).
# Overall, it results in O(n).

# Space Complexity (SC): O(1), because no additional data structures are used
# except for a few pointers (slow, fast, curr, prev), and the list is modified in place.
