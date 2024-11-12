import random

class Chance:
    walk = .3
    stop = .15
    turn_left = .175
    turn_right = .175
    turn_back = .05
    interact = .15

    def __init__(self):
        self.set_random_chance()

    def set_random_chance(self):
        values = [random.random() for _ in range(6)]
        total = sum(values)

        self.walk = values[0] / total
        self.stop = values[1] / total
        self.turn_left = values[2] / total
        self.turn_right = values[3] / total
        self.turn_back = values[4] / total
        self.interact = values[5] / total

    def update_chance(self, c_w, c_s, c_l, c_r, c_b, c_i):
        self.walk = c_w
        self.stop = c_s
        self.turn_left = c_l
        self.turn_right = c_r
        self.turn_back = c_b
        self.interact = c_i

    def default_chance(self):
        return self.update_chance(.3, .15, .175, .175, .05, .15)

    def print(self):
        print('walk: {a}'.format(a=self.walk))
        print('stop: {a}'.format(a=self.stop))
        print('turn_left: {a}'.format(a=self.turn_left))
        print('turn_right: {a}'.format(a=self.turn_right))
        print('turn_back: {a}'.format(a=self.turn_back))
        print('interact: {a}'.format(a=self.interact))
        print()