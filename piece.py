# import pygame
# import random



# class Piece():
#     def __init__(self, screen, grid_size_x=3, grid_size_y=3, start_x=25, start_y=25, step=50):
#         self.screen = screen
#         self.grid_size_x = grid_size_x
#         self.grid_size_y = grid_size_y
#         self.start_x = start_x
#         self.start_y = start_y
#         self.step = step

#     def draw(self, player, posx, posy, c_for_p1=(255, 25, 255), c_for_p2=(123, 231, 213)):
#         if player == 1:
#             pygame.draw.line(self.screen, 
#             c_for_p1,
#             (posx * self.step + self.start_x, posy * self.step + self.start_x), 
#             ((posx + 1) * self.step + self.start_x, (posy + 1) * self.step + self.start_y))

#             pygame.draw.line(self.screen, 
#             c_for_p1, 
#             ((posx + 1) * self.step + self.start_x, posy * self.step + self.start_x), 
#             (posx * self.step + self.start_x, (posy + 1) * self.step + self.start_y))
#         if player == 2:
#             pygame.draw.circle(self.screen, 
#             c_for_p2, 
#             (posx * self.step + self.start_x + self.step, posy * self.step + self.start_y + self.step), 
#             width=2)
#         else:
#             return None