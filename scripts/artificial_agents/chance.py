class Chance:
    walk = .3
    stop = .15
    turn_left = .175
    turn_right = .175
    turn_back = .05
    interact = .15

    def __init__(self):
        pass

    def update_chance(self, c_w, c_s, c_l, c_r, c_b, c_i):
        self.walk = c_w
        self.stop = c_s
        self.turn_left = c_l
        self.turn_right = c_r
        self.turn_back = c_b
        self.interact = c_i

    def default_chance(self):
        return self.update_chance(.3, .15, .175, .175, .05, .15)
