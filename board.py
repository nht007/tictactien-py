import pygame
from pygame.locals import *

from game import *
from surface import *
from board import *
from player import *
from ai import *

class Board:
    grid = None
    
    def __init__(self):
        self.grid = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
                     
    def get_possible_moves(self):
        possible_moves = []
        for row_index, col in enumerate(self.grid):
            for col_index, item in enumerate(col):
                if item is None:
                    possible_moves.append((row_index, col_index))
        return possible_moves                
        
    def game_ended(self, game):
        # check for winning rows
        for row in range(0, 3):
            if (self.grid[row][0] == self.grid[row][1] == self.grid[row][2]) \
                and (self.grid[row][0] is not None):
                
                pygame.draw.line(game.surface.background, (250,0,0), (0, (row + 1)
                    *100 - 50), (300, (row + 1)*100 - 50), 2)
                    
                return True

        # check for winning columns
        for col in range(0, 3):
            if (self.grid[0][col] == self.grid[1][col] == self.grid[2][col]) \
                and (self.grid[0][col] is not None):
                
                pygame.draw.line(game.surface.background, (250,0,0), ((col + 1)* 
                    100 - 50, 0), ((col + 1)* 100 - 50, 300), 2)
                
                return True
                
        # check for diagonal winners
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]) and \
            (self.grid[0][0] is not None):
            
            pygame.draw.line(game.surface.background, (250,0,0), (50, 50), 
                (250, 250), 2)
            
            return True

        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]) and \
            (self.grid[0][2] is not None):

            pygame.draw.line(game.surface.background, (250,0,0), (250, 50), 
                (50, 250), 2)
            
            return True
            
        # check for incomplete and cat games
        for row in self.grid:
            for item in row:
                if item is None:
                    return False # game has not ended
                    
        return True # game has ended but has no winner
