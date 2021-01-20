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
parser.add_argument('--starting', type=int, default=1, help="player to start")
parser.add_argument('--name_p1', type=str, default="ask", help="player one name")   
parser.add_argument('--name_p2', type=str, default="ask", help="player two name")   

config = parser.parse_args()

def main():
    if config.name_p1.lower() == "ask":  
        p1_name = input('''player one name
''')
    if config.name_p2.lower() == "ask":  
        p2_name = input('''player two name
''')
    x, y = s.calculate_screen_size(step=config.step, start_x=config.start_x, start_y=config.start_y)
    

    pygame.init()  # init pygame
    pygame.display.set_caption("Tic Tac Toe")  # tell pygame to name the screen Tic tac toe
    screen = pygame.display.set_mode((x, y))  # size of the game

    color_screen = (255, 255, 255)  
    pygame.Surface.fill(screen, color_screen) # fills the screen in color screen (virable)


    grid = g.Grid(screen=screen, step=config.step, start_x=config.start_x, start_y=config.start_y)
    referee = r.Referee(config.step, config.start_x, config.start_y)

    finished = False
    grid.draw_grid()

    player_turn = config.starting
    pygame.display.update()
    pygame.Surface.fill(screen, color_screen)

    while not finished:
        pygame.Surface.fill(screen, color_screen)
        grid.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True  ## Finish the game
            if event.type == pygame.MOUSEBUTTONUP:# and player_turn == 1:
                posx, posy = pygame.mouse.get_pos()
                posx_in_sq, posy_in_sq = grid.get_pos_in_square(posx, posy)
                if grid.pos_occupied(posx_in_sq, posy_in_sq):
                    grid.add_pawn(player_turn, posx_in_sq, posy_in_sq)
                    player_turn = 3 - player_turn
        
        grid.draw_all_pawns()
        pygame.display.update()
        c = referee.won(grid.occupied)
        if c == "Finish":
            finished = True
            print("finished")
        elif c == None:
            pass
        else:
            if c == 1:
                pw = p1_name
            elif c == 2:
                pw = p2_name
            print("{} won".format(pw))
            finished = True
        grid.draw_all_pawns()
        pygame.display.update()
        

if __name__ == "__main__":
    main()