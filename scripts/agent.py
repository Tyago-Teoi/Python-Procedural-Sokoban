from scripts.utils.position import Position
import random

class Chance:
    walk = .3
    stop = .3
    turn_left = .15
    turn_right = .15
    turn_back = .1
    construct = .0
    destruct = .0
    interact = .0

    def __init__(self, c_w, c_s, c_l, c_r, c_b, c_c, c_d, c_i):
        self.walk = c_w
        self.stop = c_s
        self.turn_left = c_l
        self.turn_right = c_r
        self.turn_back = c_b
        self.construct = c_c
        self.destruct = c_d
        self.interact = c_i

class Agent:
    default_chance = Chance(.3, .3, .15, .15, .1, .0, .0, .0)
    chance = None
    level = None
    position = Position(0, 0)
    facing = 'U' # U = UP, D = DOWN, L = LEFT, R = RIGHT

    def __init__(self, chance):
        self.chance = chance

    def turn(self, direction):
        if self.facing == 'U':
            self.facing = direction
        elif self.facing == 'R':
            if direction == 'R':
                self.facing = 'D'
            elif direction == 'L':
                self.facing = 'U'
            elif direction == 'D':
                self.facing = 'L'
        elif self.facing == 'D':
            if direction == 'R':
                self.facing = 'L'
            elif direction == 'L':
                self.facing = 'R'
            elif direction == 'D':
                self.facing = 'U'
        elif self.facing == 'L':
            if direction == 'R':
                self.facing = 'U'
            elif direction == 'L':
                self.facing = 'D'
            elif direction == 'D':
                self.facing = 'R'

    def walk(self):
        if self.facing == 'U':
            self.position.y += 1
        elif self.facing == 'R':
            self.position.x += 1
        elif self.facing == 'D':
            self.position.y -= 1
        elif self.facing == 'L':
            self.position.x -= 1

    def stop(self):
        pass