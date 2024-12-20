import random
from scripts.artificial_agents.agent import Agent
from scripts.level_generation.level import LevelBlock

class ConstructorAgent(Agent):
    name = "Constructor"
    chance_construct_block = 0.0
    chance_construct_box = 0.0

    def __init__(self, chance, level, environment, c_construct_block, c_construct_box):
        super().__init__(chance, level, environment)
        self.chance_construct_block = c_construct_block
        self.chance_construct_box = c_construct_box

    def interact(self):
        next_pos = self.get_next_position()
        if self.is_valid(next_pos) and self.is_walkable(next_pos):
            rand = random.uniform(0,1)
            accumulator = 0 + self.chance_construct_block
            if rand <= accumulator:
                #print('CONSTRUCT BLOCK')
                self.construct_block(next_pos)
                return
            accumulator += self.chance_construct_box
            if rand <= accumulator:
                #print('CONSTRUCT BOX')
                self.construct_box(next_pos)
                return

    def construct_block(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.LIMIT_BLOCK

    def construct_box(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.BOX_BLOCK

    def print_chance(self):
        print('CONSTRUCTOR AGENT CHANCES')
        self.chance.print()
        print('construct block: {a}'.format(a=self.chance_construct_block))
        print('construct box: {b}'.format(b=self.chance_construct_box))
        print()