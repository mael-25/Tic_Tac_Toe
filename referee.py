import random

class Referee:
    def __init__(self):
        self.occupied = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.b = 0
        self.c = 0