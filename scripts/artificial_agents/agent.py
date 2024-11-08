from scripts.utils.position import Position
import random


class Agent:
    chance = None
    player_params = None
    level = None
    position = Position(0, 0)
    facing = 'U' # U = UP, D = DOWN, L = LEFT, R = RIGHT

    def __init__(self, chance, player_params):
        self.chance = chance
        self.player_params = player_params

    def act(self):
        rand = random.uniform(0,1)
        accumulator = 0 + self.chance.walk

        if rand < accumulator:
            self.walk()
        accumulator += self.chance.stop
        if rand < accumulator:
            self.stop()
        accumulator += self.chance.turn_left
        if rand < accumulator:
            self.turn('L')
        accumulator += self.chance.turn_right
        if rand < accumulator:
            self.turn('R')
        accumulator += self.chance.turn_back
        if rand < accumulator:
            self.turn('D')
        accumulator += self.chance.interact
        if rand < accumulator:
            self.interact()            

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
        self.position = self.get_next_position()

    def stop(self):
        pass

    def interact(self):
        pass

    def get_next_position(self):
        next_position = Position(self.position.x, self.position.y)

        if self.facing == 'U':
            next_position.y += 1
        elif self.facing == 'R':
            next_position.x += 1
        elif self.facing == 'D':
            next_position.y -= 1
        elif self.facing == 'L':
            next_position.x -= 1

        return next_position