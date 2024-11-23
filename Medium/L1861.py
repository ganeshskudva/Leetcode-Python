class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box:
            return []
        
        m, n = len(box), len(box[0])  # Dimensions of the box
        stone, obstacle, empty = '#', '*', '.'
        
        # Step 1: Simulate gravity for each row
        for row in box:
            move_position = n - 1  # Start from the last position in the row
            for j in range(n - 1, -1, -1):  # Traverse the row from right to left
                if row[j] == obstacle:  # Reset move position when an obstacle is found
                    move_position = j - 1
                elif row[j] == stone:  # Move stone to the nearest available position
                    if j != move_position:  # Only swap if the positions are different
                        row[j], row[move_position] = row[move_position], row[j]
                    move_position -= 1  # Move the position for the next stone

        # Step 2: Rotate the box clockwise
        rotated_box = []
        for i in range(n):  # Iterate through columns of the original box
            rotated_box.append([box[j][i] for j in range(m - 1, -1, -1)])  # Build the rotated rows
        
        return rotated_box

# Time Complexity (TC):
# Step 1: Simulating gravity involves traversing each element in the `box` once.
#         This takes O(m * n), where `m` is the number of rows and `n` is the number of columns.
# Step 2: Rotating the box requires traversing each element again to build the rotated grid.
#         This also takes O(m * n).
# Overall Time Complexity: O(m * n)

# Space Complexity (SC):
# - The `rotated_box` requires additional space to store the rotated grid, which is O(m * n).
# - No other significant auxiliary space is used.
# Overall Space Complexity: O(m * n)
