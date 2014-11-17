import pygame
from pygame.locals import *

from game import *
from surface import *
from board import *
from player import *
from ai import *

class Game:
    surface = None
    board = None
    player_one = None # plays X
    player_two = None # plays O
    current_player = None
    
    def __init__(self, player_one, player_two):
        self.surface = Surface()
        self.board = Board()
        self.player_one = player_one
        self.player_two = player_two
        
        self.event_loop() # starts the main event loop
    
    def event_loop(self):
        running = True
        ended = False
        self.current_player = self.player_one
        
        while running:
            for event in pygame.event.get():
                if event.type is QUIT:
                    running = False
                elif event.type is MOUSEBUTTONDOWN:
                    if not ended:
                        self.current_player.perform_move(self)
            
            # check for three in a row
            ended_temp = self.board.game_ended(self)
            
            # update the display
            if not ended:
                self.surface.redraw_surface()
            
            ended = ended_temp
            
    def switch_player(self):
        if self.current_player is self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

