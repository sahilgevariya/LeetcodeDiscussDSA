'''
    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turnRight();

      // Clean the current cell.
      void clean();
    }
    
        Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
    Output: Robot cleaned all rooms.
'''

# TC : (Total_cells - Obstacle_cells)
# SC : (Total_cells - Obstacle_cells)
class Solution:
    def cleanRoom(self, robot):
        def undo_move():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(x, y, cur_direction):
            visited.add((x, y))
            robot.clean()
            
            # try all four directions
            for next_direction in range(4):
                new_dir = (cur_direction + next_direction) % 4  # re-calc the direction tag
                new_x = x + directions[new_dir]
                new_y = y + directions[new_dir + 1]
                
                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_dir)
                    undo_move()
                    
                robot.turnRight()   # turn the orientation/face of robot to next direction (clockwise)

        directions = (-1, 0, 1, 0, -1)    # 0 -> up, 1 -> right, 2 -> down, 3 -> left
        visited = set()
        backtrack(0, 0, 0)    # considering startin position (0,0) and init directio is up (0)
        
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
