import os
import random 


class Maze_Crawler:
    def __init__(self, blocks_per_row: int, row_length: int):
        self.maze = []
        self.blocks_per_row = blocks_per_row
        self.row_length = row_length 
    

    def generate_binary_string(self, n: int): 
        base_list = ["1", "0"]
        for i in range(n-1): 
            updated_list = []
            for element in base_list:
                new_value_w0  = element + "0"
                new_value_w1  = element + "1"
                updated_list.append(new_value_w1)
                updated_list.append(new_value_w0) 
            base_list = updated_list 

        return updated_list 


    def generate_maze(self, blocks_per_row: int, row_length: int): 
        possible_outcomes = self.generate_binary_string(row_length) 
        qualified_outcomes = []

        # Generate Maze through binary generator
        for outcome in possible_outcomes: 
            binary_list = list(outcome)
            outcome_total = sum(int(x) for x in binary_list)
            if outcome_total == blocks_per_row: 
                qualified_outcomes.append(outcome) 

        # Shuffle the result from the generator 
        qualified_outcomes = random.sample(qualified_outcomes, len(qualified_outcomes))

        # Adding Starting position as S at the first position for first row 
        first_str = qualified_outcomes[0]
        first_str = "S" + first_str[1:]
        qualified_outcomes[0] = first_str

        # Adding Ending position as E at the last position of last row 
        last_str = qualified_outcomes[row_length - 1]
        last_str = last_str[:-1] + "E" 
        qualified_outcomes[row_length - 1] = last_str 

        # Adding Top and Bottome Walls as 1
        qualified_outcomes.insert(0, "1" * row_length)
        qualified_outcomes.append("1" * row_length) 

        # Adding Left and Right Walls as 1 
        for i in range(len(qualified_outcomes)): 
            qualified_outcomes[i] = "1" + qualified_outcomes[i] + "1"

        return qualified_outcomes


    def load_maze(self):
        # Get generated binary 
        rows = self.generate_maze(self.blocks_per_row, self.row_length)
        
        # Convert generated binary into list of list 
        for i in range(len(rows)):
            self.maze.append([])
        
            for j in range(len(rows[i])):
                self.maze[i].append(rows[i][j])

        return self.maze
    

    def get_start_coor(self):
        # Get starting co-ordinate of S as starting position 
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    return i, j
        return -1, -1
    

    def solve_maze(self, coor: tuple[int, int]):
        x, y = coor
        
        # Avoid walls (1) and blocks (X) that has been walked on 
        if self.maze[x][y] == '1' or self.maze[x][y] == 'X':
            return False
        
        # Check if arrived at target position 
        if self.maze[x][y] == 'E':
            return True
        
        # Set the block to X to notify if it had been walked on
        if self.maze[x][y] != 'S':
            self.maze[x][y] = 'X'
        
        # Moving strategy 
        if self.solve_maze((x+1, y)):
            if self.maze[x][y] != 'S':
                self.maze[x][y] = 'v'
            
        elif self.solve_maze((x-1, y)):
            if self.maze[x][y] != 'S':
                self.maze[x][y] = '^'
            
        elif self.solve_maze((x, y+1)):
            if self.maze[x][y] != 'S':
                self.maze[x][y] = '>'
            
        elif self.solve_maze((x, y-1)):
            if self.maze[x][y] != 'S':
                self.maze[x][y] = '<'
        else:
            return False
        
        return True
    

    def show_maze(self):
        for row in range(len(self.maze)): 
            maze_row = self.maze[row]
            for element in range(len(maze_row)): 
                # Replace X to clean up blocks that we had walked on but not in the final solution
                # Example are blocks that don't have forward position so need to go backward 
                if maze_row[element] == "X": 
                    maze_row[element] = "0"
            print(maze_row) 


if __name__ == "__main__": 
    maze = Maze_Crawler(1, 7)
    # Show Maze current map
    print("GENERATED MAZE: ")
    maze.load_maze()
    maze.show_maze()

    print("\r\n######################################################\r\n")
    print("SOLUTION: ")
    start = maze.get_start_coor()
    # Show Maze solution 
    maze.solve_maze(start) 
    maze.show_maze()    

