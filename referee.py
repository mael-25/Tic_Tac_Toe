import random

class Referee:
    def __init__(self, step, start_x, start_y):
        pass
    def line_check(self, occupied):
        for y in range(len(occupied)):
            if occupied[y] == [1, 1, 1]:
                return 1
            if occupied[y] == [2, 2, 2]:
                return 2

    def column_check(self, occupied):
        for y in range(len(occupied)):
            column_occupied = []
            for x in range(len(occupied)):
                column_occupied.append(occupied[y][x])
            if column_occupied == [1, 1, 1]:
                return 1
            if column_occupied == [2, 2, 2]:
                return 2

    def diagonal_check(self, occupied):
        diagonal_occupied = []
        for yx in range(len(occupied)):
            diagonal_occupied.append(occupied[yx][yx])
        if diagonal_occupied == [1, 1, 1]:
            return 1
        if diagonal_occupied == [2, 2, 2]:
            return 2


        diagonal_occupied = []
        for y in range(len(occupied)):
            x = 2 - y
            diagonal_occupied.append(occupied[y][x])
        if diagonal_occupied == [1, 1, 1]:
            return 1
        if diagonal_occupied == [2, 2, 2]:
            return 2

    def check_draw(self, occupied):
        # value = True
        for y in range(len(occupied)):
            for x in range(len(occupied)):
                if occupied[y][x] == 0:
                    return None

        return "Finish"

    def won(self, occupied):
        a = self.line_check(occupied)
        b = self.column_check(occupied)
        c = self.diagonal_check(occupied)
        d = self.check_draw(occupied)

        if a != 0:
            return a
        if b != 0:
            return b
        if c != 0:
            return c
        if d == "Finish":
            return "Finish"
        return None
        