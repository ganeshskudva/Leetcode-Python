# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])  # Queue for level-order traversal (BFS)
        min_heap = []  # Min-heap to store the top k largest level sums

        # Perform level-order traversal
        while q:
            sz, tot = len(q), 0  # sz is the number of nodes at the current level
            for _ in range(sz):
                node = q.popleft()  # Remove the front node from the queue
                tot += node.val  # Add the value of the current node to the level sum

                # Add the left and right children of the current node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Keep only the top k largest sums in the min-heap
            if len(min_heap) < k:
                heappush(min_heap, tot)  # Add the current level sum if heap is not full
            else:
                # If the heap is full, replace the smallest sum if the current sum is larger
                if tot > min_heap[0]:
                    heapreplace(min_heap, tot)

        # If there are fewer than k levels, return -1
        if len(min_heap) < k:
            return -1

        # The kth largest level sum will be the smallest element in the min-heap
        return min_heap[0]

# Time Complexity (TC):
# - The level-order traversal (BFS) processes each node once, taking O(N), where N is the number of nodes in the tree.
# - For each level, we perform heap operations. In the worst case, we maintain a heap of size k.
# - Inserting into and replacing elements in the heap takes O(log k) time.
# - Therefore, the overall time complexity is O(N log k), where N is the number of nodes and k is the size of the heap (or the kth largest level sum).

# Space Complexity (SC):
# - The queue (q) for the level-order traversal can hold at most O(W) nodes, where W is the maximum width of the tree. In the worst case, W = N/2.
# - The min-heap stores at most k elements, so the space required for the heap is O(k).
# - Overall space complexity is O(W + k), where W is the maximum width of the tree, and k is the number of elements we store in the heap.
