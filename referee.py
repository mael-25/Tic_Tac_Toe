import random

class Referee:
    def __init__(self, step, start_x, start_y):
        self.occupied = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        self.step = step
        self.start_x = start_x
        self.start_y = start_y
    
    def choose_pos(self, occupied):
        self.occupied = occupied
        if self.occupied[1][1] == 0:
            print("center not occupied, taking center")
            return 1, 1
        if self.occupied[1][1] == 1:
            lst_r = [(0, 2), (0, 0), (2, 2), (2, 0)]
            if self.occupied[0][2] == 2:
                lst_r = [None]
            if self.occupied[2][2] == 2:
                lst_r = [None]
            if self.occupied[0][0] == 2:
                lst_r = [None]
            if self.occupied[2][0] == 2:
                lst_r = [None]


            if self.occupied[0][2] == 1:
                lst_r.remove([0, 2])
            if self.occupied[2][2] == 2:
                lst_r.remove([2, 2])
            if self.occupied[0][0] == 2:
                lst_r.remove([0, 0])
            if self.occupied[2][0] == 2:
                lst_r.remove([2, 0])

            random.shuffle(lst_r)
            take = lst_r[0]
            x = take[0] * self.step + self.start_x
            y = take[1] * self.step + self.start_y

            return x, y

        
                