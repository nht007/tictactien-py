import pygame
from pygame.locals import *

from game import *
from surface import *
from board import *
from player import *
from ai import *

class Surface:
    background = None
    window = None
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((300,300))
        pygame.display.set_caption('Tic Tac Toe')
        
        # set up the background surface
        self.background = pygame.Surface(self.window.get_size())
        self.background = self.background.convert()
        self.background.fill ((250, 250, 250))

        # draw the grid lines
        pygame.draw.line (self.background, (0,0,0), (100, 0), (100, 300), 2)
        pygame.draw.line (self.background, (0,0,0), (200, 0), (200, 300), 2)

        pygame.draw.line (self.background, (0,0,0), (0, 100), (300, 100), 2)
        pygame.draw.line (self.background, (0,0,0), (0, 200), (300, 200), 2)
        
    def redraw_surface(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()
        
    def draw_move(self, surface_pos, player):
        (row, col) = surface_pos
        
        # determine the center of the selected square
        center_x = (col * 100) + 50
        center_y = (row * 100) + 50
        
        if player == 'X':
            pygame.draw.line(self.background, (0,0,0), (center_x - 22, center_y 
                - 22), (center_x + 22, center_y + 22), 2)
            pygame.draw.line(self.background, (0,0,0), (center_x + 22, center_y 
                - 22), (center_x - 22, center_y + 22), 2)
        else: # if player == 'O'
            pygame.draw.circle(self.background, (0,0,0), (center_x, center_y), 
                44, 2)
