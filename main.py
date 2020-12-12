import pygame
import argparse
import time
import sys

import screen as s
import grid as g
import piece as p
import referee as r

parser = argparse.ArgumentParser()
parser.add_argument('--step', type=int, default=50)
parser.add_argument('--start_x', type=int, default=25, help="pixel to start x")
parser.add_argument('--start_y', type=int, default=25, help="pixel to start y")
parser.add_argument('--starting', type=int, default=1, help= "player to start(1 for player, 2 for computer)")

config = parser.parse_args()

def main():
    

    x, y = s.calculate_screen_size(step=config.step, start_x=config.start_x, start_y=config.start_y)
    

    pygame.init()  # init pygame
    pygame.display.set_caption("Tic Tac Toe")  # tell pygame to name the screen Tic tac toe
    screen = pygame.display.set_mode((x, y))  # size of the game

    color_screen=(255,255,255)  
    pygame.Surface.fill(screen, color_screen) # fills the screen in color screen (virable)


    grid_ = g.Grid(screen=screen, step=config.step, start_x=config.start_x, start_y=config.start_y)
    piece = p.Piece(screen, 3, 3, config.start_x, config.start_y, config.step)    
    referee = r.Referee(config.step, config.start_x, config.start_y)

    finished = False
    grid_.draw_grid()

    player_turn = config.starting
    pygame.display.update()

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True  ## Finish the game
            if event.type == pygame.MOUSEBUTTONUP and player_turn == 1:
                posx, posy = pygame.mouse.get_pos()
                posx_in_sq, posy_in_sq = grid_.get_pos_in_square(posx, posy)
                if grid_.pos_occupied(posx_in_sq, posy_in_sq):
                    grid_.add_pawn(1, posx_in_sq, posy_in_sq)
                    piece.draw(1, posx_in_sq, posy_in_sq)
                    player_turn = 2
        
        grid_.draw_all_pawns()
        pygame.display.update()

        print(grid_.occupied)
        if player_turn == 2:
            posx_in_sq, posy_in_sq = grid_.get_pos_in_square(x, y)
            player_turn = 1
            grid_.add_pawn(2, posx_in_sq, posy_in_sq)
            grid_.change_occupied(grid_.occupied)

        grid_.draw_all_pawns()
        pygame.display.update()
        

if __name__ == "__main__":
    main()