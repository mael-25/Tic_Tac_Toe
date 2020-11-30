import pygame


class Grid:
    def __init__(self, screen, start_x=25, start_y=25, step=50, grid_size_x=3, grid_size_y=3):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.step = step
        self.occupied = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def draw_grid(self):
        for x in range(1, 3):             
            pygame.draw.line(
                self.screen, 
                (0, 0, 0), 
                (self.start_x, self.start_y+self.step*x), 
                (self.start_x+self.step*3, self.start_y+self.step*(x)))

        for y in range(1, 3):
            pygame.draw.line(
                self.screen, 
                (0, 0, 0), 
                (self.start_x+self.step*y, self.start_y), 
                (self.start_x+self.step*y, self.start_y+self.step*3))

    def draw_all_pawns(self):
        for y in self.occupied:
            for x in y:
                if x == 0: ## not occupied
                    pass
                if x == 1: ## occupied by player 1
                    pass
                if x == 2: ## occupied by player 2
                    pass

    
        
    def add_pawn(self, player, posx_sq, posy_sq):
        if self.occupied[posx_sq][posy_sq] == 0:

            if player == 1:
                self.occupied[posx_sq][posy_sq] = 1
                # print(pos)

                return True
            if player == 2:
                self.occupied[posx_sq][posy_sq] = 2
                # print(pos)
                return True
        else: 
            return False

    
    def get_pos_in_square(self, posx, posy):
        new_pos_x = (posx - self.start_x) // self.step
        new_pos_y = (posy - self.start_y) // self.step
        if new_pos_x < 4 or new_pos_y < 4: ##or new_pos_x != 0 or new_pos_y != 0:
            return new_pos_x, new_pos_y
        return None

    def pos_occupied(self, posx_sq, posy_sq):
        print(posx_sq, posy_sq)
        if posx_sq < 3 and \
            posx_sq >= 0 and \
            posy_sq < 3 and \
            posy_sq >= 0:

            if self.occupied[posx_sq][posy_sq] == 0:
                return True
            else:
                return False
        else:
            return False