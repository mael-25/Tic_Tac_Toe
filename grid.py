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

    def draw(self, player, posx, posy, c_for_p1=(255, 25, 255), c_for_p2=(123, 231, 213)):
        if player == 1:
            pygame.draw.line(self.screen, 
            c_for_p1,
            (posx * self.step + self.start_x, posy * self.step + self.start_x), 
            ((posx + 1) * self.step + self.start_x, (posy + 1) * self.step + self.start_y))

            pygame.draw.line(self.screen, 
            c_for_p1, 
            ((posx + 1) * self.step + self.start_x, posy * self.step + self.start_x), 
            (posx * self.step + self.start_x, (posy + 1) * self.step + self.start_y))
        if player == 2:
            pygame.draw.circle(self.screen, 
            c_for_p2, 
            (posx * self.step + self.step/2 + self.start_x, posy * self.step + self.step/2 + self.start_y), 
            self.step / 2, 
            width=2)
        else:
            return None
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

    def draw_all_pawns(self, c1=(25, 255, 0), c2=(12, 100, 255)):
        # for y in self.occupied:
        #     for x in y:
        #         if x == 0: ## not occupied
        #             pass
        #         if x == 1: ## occupied by player 1
        #             pass
        #         if x == 2: ## occupied by player 2
        #             pass
        self.draw_grid()
        for y in range(3):
            for x in range(3):
                self.draw(self.occupied[y][x], x, y)

    
        
    def add_pawn(self, player, posx_sq, posy_sq):
        if self.occupied[posy_sq][posx_sq] == 0:

            if player == 1:
                self.occupied[posy_sq][posx_sq] = 1
                # print(pos)

                return True
            if player == 2:
                self.occupied[posy_sq][posx_sq] = 2
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

            if self.occupied[posy_sq][posx_sq] == 0:
                return True
            else:
                return False
        else:
            return False

    def change_occupied(self, new_occupied):
        self.occupied = new_occupied