import random

class Referee():
    def __init__(self, step, start_x, start_y):
        # self.occupied = [
        #     [0, 0, 0],
        #     [0, 0, 0],
        #     [0, 0, 0]]
        # self.step = step
        # self.start_x = start_x
        # self.start_y = start_y
        pass

    def player_wins(self, occupied):
        pass

    # return a coordinate if player can win
    def player_will_win(self, player, occupied):
        # let a player play and see if there is a winning position

        pass
    
    def choose_pos(self, player, occupied):
        # choose random position


        # can the player win (if player can win, then select the correct position and return)

        # check if the other player can win (if the other player can win, player will select the winning position)

        # Choose the center if available

        # Choose the best corner if availlable

        # random (choose whichever free position)



        # # self.occupied = occupied
        # if occupied[1][1] == 0:
        #     print("take center")
        #     occupied[1][1] = 2
        #     return 1, 1, occupied
        
        # for ox in range(3):
        #     for oy in range(3):
        #         if occupied[ox] == [0, 2, 2]\
        #             or occupied[ox] == [2, 0, 2]\
        #             or occupied[ox] == [2, 2, 0]:

        #             occupied[ox] = [2, 2, 2]
        #             if occupied[ox][oy] == 0:
        #                 return ox, oy, occupied
                
                
        #         if occupied[ox] == [0, 1, 1]\
        #             or occupied[ox] == [1, 0, 1]\
        #             or occupied[ox] == [1, 1, 0]:
                    
        #             # new_occupied = occupied[ox]
        #             for o in range(3):
        #                 if occupied[ox][o] == 0:
        #                     occupied[ox][o] = 2
        #             if occupied[ox][oy] == 0:
        #                 return ox, oy, occupied

        
        # for ox in range(3):
        #     colum = []
        #     for oy in range(3):
        #         colum.append(occupied[oy])
        #         if colum[oy] == 1:
        #             break
                
        #         if oy == 2:                    
        #             if colum == [0, 2, 2] or \
        #                 colum == [2, 0, 2] or \
        #                 colum == [2, 2, 0]:

        #                 for y in range(3):
        #                     if occupied[ox][y] == 0:
        #                         return ox, y, occupied


        #             if colum == [0, 1, 1] or \
        #                 colum == [1, 0, 1] or \
        #                 colum == [1, 1, 0]:

        #                 for y in range(3):
        #                     if occupied[ox][y] == 0:
        #                         return ox, y, occupied
        # print("WARNING")
        return None, None, None

    def winner(self, occupied):
        # for x in occupied:
        #     c = []
        #     if x == [1, 1, 1]:
        #         return 1
        #     if x == [2, 2, 2]:
        #         return 2
        #     for y in x:
        #         c.append(y)
            
        #     if c == [1, 1, 1]:
        #         return 1
        #     if c == [2, 2, 2]:
        #         return 2
        
        # a = None
        
        # for x in occupied:
        #     for y in x:
        #         if y == 0:
        #             a = False
        #             return None
        
        # if a == None:
        #     return 0
        for x in range(3):
            for y in range(3):
                pass