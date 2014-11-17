class MiniMax:
    value = None
    last_move = None
    grid = None
    token = None
    root_token = None
    children = None
    
    def __init__(self, last_move, grid, token, root_token):
        self.last_move = last_move
        self.grid = grid
        self.token = token
        self.root_token = root_token
        
    def build_tree(self):
        evaluation = self._evaluate()
        if evaluation is not False:
            self.value = evaluation
            return
            
        moves = self._get_possible_moves()
        
        self.children = []
        for move in moves:
            row, col = move
            next_grid = self._deepcopy(self.grid)
            next_grid[row][col] = self.token
            
            self.children.append(MiniMax(move, next_grid, self._switch_token(), 
                self.root_token))
              
        value_list = []
        for child in self.children:
            child.children = []
            child.build_tree()
            value_list.append(child.value)
            
        if self.token == self.root_token:
            self.value = max(value_list)
        else:
            self.value = min(value_list)
        
    def get_next_move(self):
        child_list = []
        for child in self.children:
            child_list.append((child.last_move,child.value))
        
        (move_list, value_list) = zip(*child_list)
        
        return move_list[value_list.index(max(value_list))]
                
    # required because python doesn't allow deepcopy of instance members
    def _deepcopy(self, grid):
        return [list(grid[0]),
                    list(grid[1]),
                    list(grid[2])]
        
    def _get_possible_moves(self):
        possible_moves = []
        for row_index, col in enumerate(self.grid):
            for col_index, item in enumerate(col):
                if item is None:
                    possible_moves.append((row_index, col_index))
        return possible_moves     
        
    def _switch_token(self):
        if self.token == 'X':
            return 'O'
        else:
            return 'X'
            
    def _evaluate(self):
        # check for winning rows
        for row in range(0, 3):
            if (self.grid[row][0] == self.grid[row][1] == self.grid[row][2]) \
                and (self.grid[row][0] is not None):
                    
                if self.grid[row][0] == self.root_token:
                    return 1
                else:
                    return -1

        # check for winning columns
        for col in range(0, 3):
            if (self.grid[0][col] == self.grid[1][col] == self.grid[2][col]) \
                and (self.grid[0][col] is not None):
                
                if self.grid[0][col] == self.root_token:
                    return 1
                else:
                    return -1
                
        # check for diagonal winners
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]) and \
            (self.grid[0][0] is not None):
            
            if self.grid[0][0] == self.root_token:
                return 1
            else:
                return -1

        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]) and \
            (self.grid[0][2] is not None):
            
            if self.grid[0][2] == self.root_token:
                return 1
            else:
                return -1
                    
        # check for incomplete and cat games
        for row in self.grid:
            for item in row:
                if item is None:
                    return False # game has not ended
                    
        return 0 # game has ended but has no winner
