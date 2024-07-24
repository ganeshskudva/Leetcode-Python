class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        num_columns = len(grid[0])
        
        # Calculate the total sum of the top row
        total_top_row_sum = sum(grid[0])
        cumulative_top_row_sum = 0
        cumulative_bottom_row_sum = 0
        max_second_robot_score = 0

        # Initialize cumulative sums
        cumulative_bottom_row_sum = 0

        # Iterate through each column to compute the maximum score
        for col in range(num_columns):
            cumulative_top_row_sum += grid[0][col]
            cumulative_bottom_row_sum += grid[1][col]
            remaining_top_row_sum = total_top_row_sum - cumulative_top_row_sum
            max_second_robot_score = max(max_second_robot_score, min(remaining_top_row_sum, cumulative_bottom_row_sum))
        
        return max_second_robot_score
