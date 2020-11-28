import pygame
import random



class Piece:
    def __init__(self, screen, grid_size_x=3, grid_size_y=3, start_x=25, start_y=25, step=50):
        self.screen = screen
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.start_x = start_x
        self.start_y = start_y
        self.step = step

    def draw(self, player, posx, posy):
        if player == 1:
            r1 = random.randint(0, 255)
            r2 = random.randint(0, 255)
            r3 = random.randint(0, 255)
            pygame.draw.line(self.screen, 
            (r1, r2, r3), 
            (posx * self.step + self.start_x, posy * self.step + self.start_x), 
            ((posx + 1) * self.step + self.start_x, (posy + 1) * self.step + self.start_y))

            pygame.draw.line(self.screen, 
            (r2, r3, r1), 
            ((posx + 1) * self.step + self.start_x, posy * self.step + self.start_x), 
            (posx * self.step + self.start_x, (posy + 1) * self.step + self.start_y))
        if player == 2:
            pass
        else:
            return None