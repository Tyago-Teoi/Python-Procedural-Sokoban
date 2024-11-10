from scripts.utils.position import Position
import random

class Agent:
    chance = None
    player_params = None
    level = None
    position = Position(0, 0)
    facing = 'U' # U = UP, D = DOWN, L = LEFT, R = RIGHT

    def __init__(self, chance, level, player_params):
        self.chance = chance
        self.level = level
        self.player_params = player_params
        self.set_agent_spawn_position()

    def act(self):
        rand = random.uniform(0,1)
        accumulator = 0 + self.chance.walk

        if rand < accumulator:
            print("WALK")
            self.walk()
            return
        accumulator += self.chance.stop
        if rand < accumulator:
            print("STOP")
            self.stop()
            return
        accumulator += self.chance.turn_left
        if rand < accumulator:
            print("TURN_LEFT")
            self.turn('L')
            return
        accumulator += self.chance.turn_right
        if rand < accumulator:
            print("TURN_RIGHT")
            self.turn('R')
            return
        accumulator += self.chance.turn_back
        if rand < accumulator:
            print("TURN_BACK")
            self.turn('D')
            return
        accumulator += self.chance.interact
        if rand < accumulator:
            print("INTERACT")
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
        print("AAAAAAAAAAAAAAAAA")
        print(len(self.level[0]) - 1)
        print(len(self.level) - 1)
        print("AAAAAAAAAAAAAAAA")
        x = random.randint(1, len(self.level[0]) - 1)
        y = random.randint(1, len(self.level) - 1)
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

        last_position.print()
        next_position.print()
        print('{a} {b}'.format(a=self.is_valid(next_position), b=self.is_walkable(next_position)))
        if self.is_valid(next_position) and self.is_walkable(next_position):
            return next_position
        return last_position

    def is_valid(self, pos):
        return 1 <= pos.y < len(self.level) and 1 <= pos.x < len(self.level[0])

    def is_walkable(self, pos):
        return self.level[pos.y][pos.x] != "#" and self.level[pos.y][pos.x] != "$"