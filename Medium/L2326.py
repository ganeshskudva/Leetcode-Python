# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
            i, j, cur_d = 0, 0, 0
            d = [0, 1, 0, -1, 0]  # direction array for movement
            res = [[-1] * n for _ in range(m)]  # initializing matrix with -1

            while head:
                res[i][j] = head.val  # assign value
                head = head.next  # move to next node

                # calculate next position
                ni, nj = i + d[cur_d], j + d[cur_d + 1]

                # check boundary conditions and if the cell is already filled
                if min(ni, nj) < 0 or ni >= m or nj >= n or res[ni][nj] != -1:
                    cur_d = (cur_d + 1) % 4  # change direction

                i += d[cur_d]  # update row index
                j += d[cur_d + 1]  # update column index

            return res
        
