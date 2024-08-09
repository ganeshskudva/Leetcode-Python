class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Initialize the starting position and direction (north)
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West

        # Movements corresponding to the directions: North, East, South, West
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = movements[direction]
                x, y = x + dx, y + dy
            elif instruction == 'L':
                direction = (direction - 1) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4

        # Check if the robot is back at the origin or not facing North
        return (x == 0 and y == 0) or direction != 0
