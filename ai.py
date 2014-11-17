import pygame
from pygame.locals import *
from random import choice

from game import *
from surface import *
from board import *
from player import *
from ai import *
from minimax import *

class AI:
    def __init__(self):
        pass
    
    
class RandomAI(AI):
    def __init__(self):
        AI()
    
    def find_move(self, game, current_player):
        possible_moves = game.board.get_possible_moves()
        return choice(possible_moves)
        
        
class PerfectAI(AI):
    player_token = None
    
    def __init__(self):
        AI()
        
    def find_move(self, game, current_player):
        # Optimization: Avoid lengthy minimax call if perfect AI
        #   is first to move.
        if len(game.board.get_possible_moves()) == 9:
            return (0,0)
            
        if current_player is game.player_one:
            self.player_token = 'X'
        else:
            self.player_token = 'O'
            
        root = MiniMax(None, game.board.grid, self.player_token, 
            self.player_token)
        root.build_tree()
        
        return root.get_next_move()

