import pygame
from pygame.locals import *

from game import *
from surface import *
from board import *
from player import *
from ai import *

class Player:
    
    def __init__(self):
        pass
        
    def _execute_move(self, game, board_pos):
        (row, col) = board_pos
        
        # only handle click if space is untaken
        if game.board.grid[row][col] is None:
            if game.current_player is game.player_one:
                game.surface.draw_move(board_pos, 'X')
                game.board.grid[row][col] = 'X' # if player is X
            else:
                game.surface.draw_move(board_pos, 'O')
                game.board.grid[row][col] = 'O' # if player is O
            game.switch_player()
            return True
        return False


class HumanPlayer(Player):
    def __init__(self):
        Player()
        
    def perform_move(self, game):
        mouse_pos = pygame.mouse.get_pos()
        board_pos = self._get_board_pos(mouse_pos)
        
        return self._execute_move(game, board_pos)
        
    def _get_board_pos(self, mouse_pos):
        (mouse_x, mouse_y) = mouse_pos
        
        if mouse_y < 100:
            row = 0
        elif mouse_y < 200:
            row = 1
        else:
            row = 2
            
        if mouse_x < 100:
            col = 0
        elif mouse_x < 200:
            col = 1
        else:
            col = 2
        
        return (row, col)
        
              
class CPUPlayer(Player):
    ai = None
    
    def __init__(self, ai=PerfectAI()):
        Player()
        self.ai = ai
    
    def perform_move(self, game):
        board_pos = self.ai.find_move(game, self)
        
        return self._execute_move(game, board_pos)
