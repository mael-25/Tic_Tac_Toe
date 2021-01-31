import random

class Referee:
    def __init__(self, step, start_x, start_y):
        pass
    def line_check(self, occupied):
        ## works
        for y in range(len(occupied)):
            if occupied[y] == [1, 1, 1]:
                # print(1)
                return 1
                
            if occupied[y] == [2, 2, 2]:
                # print(2)
                return 2

        return None
                

    def column_check(self, occupied):
        for y in range(len(occupied)):
            column_occupied = []
            for x in range(len(occupied[y])):
                # print(occupied)
                column_occupied.append(occupied[x][y])
            if column_occupied == [1, 1, 1]:
                # print(1)
                return 1
            if column_occupied == [2, 2, 2]:
                # print(2)
                return 2

        return None

    def diagonal_check(self, occupied): #works
        diagonal_occupied = []
        for yx in range(len(occupied)):
            diagonal_occupied.append(occupied[yx][yx])
        if diagonal_occupied == [1, 1, 1]:
            
            return 1 
        if diagonal_occupied == [2, 2, 2]:
            # print(2)
            return 2 

        


        diagonal_occupied = []
        for y in range(len(occupied)):
            x = 2 - y
            diagonal_occupied.append(occupied[y][x])
        if diagonal_occupied == [1, 1, 1]:
            # print(1)
            return 1
            
        if diagonal_occupied == [2, 2, 2]:
            # print(2)
            return 2

        return None
            

    def check_full(self, occupied):
        # value = True
        for y in range(len(occupied)):
            for x in range(len(occupied)):
                if occupied[y][x] == 0:
                    return None

        return "Finish"

    def won(self, occupied):
        line = self.line_check(occupied)
        column = self.column_check(occupied)
        diagonal = self.diagonal_check(occupied)
        draw = self.check_full(occupied)
        if line != None:
            return line
        if column != None:
            return column
        if diagonal != None:
            return diagonal
        if draw == "Finish":
            return "Finish"
        return None
        