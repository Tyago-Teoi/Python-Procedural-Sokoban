from scripts.utils.position import Position
import random

class Agent:
    name = "Generic"
    chance = None
    environment = None
    level = None
    position = Position(0, 0)
    facing = 'U' # U = UP, D = DOWN, L = LEFT, R = RIGHT

    def __init__(self, chance, level, environment):
        self.chance = chance
        self.level = level
        self.environment = environment
        self.set_agent_spawn_position()

    def act(self):
        rand = random.uniform(0,1)
        accumulator = 0 + self.chance.walk

        if rand < accumulator:
            self.walk()
            return
        accumulator += self.chance.stop
        if rand < accumulator:
            self.stop()
            return
        accumulator += self.chance.turn_left
        if rand < accumulator:
            self.turn('L')
            return
        accumulator += self.chance.turn_right
        if rand < accumulator:
            self.turn('R')
            return
        accumulator += self.chance.turn_back
        if rand < accumulator:
            self.turn('D')
            return
        accumulator += self.chance.interact
        if rand < accumulator:
            self.interact()
            return

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

    def set_agent_spawn_position(self):
        x = random.randint(1, self.environment.width - 1)
        y = random.randint(1, self.environment.height - 1)
        self.position = Position(x, y)

    def get_next_position(self):
        last_position = Position(self.position.x, self.position.y)
        next_position = Position(self.position.x, self.position.y)

        if self.facing == 'U':
            next_position.y += 1
        elif self.facing == 'R':
            next_position.x += 1
        elif self.facing == 'D':
            next_position.y -= 1
        elif self.facing == 'L':
            next_position.x -= 1

        if self.is_valid(next_position) and self.is_walkable(next_position):
            return next_position
        return last_position

    def is_valid(self, pos):
        return 1 <= pos.y <= self.environment.height and 1 <= pos.x <= self.environment.width

    def is_walkable(self, pos):
        return self.level[pos.y][pos.x] != "#" and self.level[pos.y][pos.x] != "$"