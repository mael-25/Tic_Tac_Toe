import pygame


class Piece:
    def __init__(self, screen, grid_size_x=3, grid_size_y=3, start_x=25, start_y=25, step=50):
        self.screen = screen
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.start_x = start_x
        self.start_y = start_y
        self.step = step