import random
from scripts.artificial_agents.agent import Agent
from scripts.level import LevelBlock

class ConstructorAgent(Agent):
    name = "Constructor"
    chance_construct_block = 0.0
    chance_construct_box = 0.0

    def __init__(self, chance, player_params, level, c_construct_block, c_construct_box):
        super().__init__(chance, level, player_params)
        self.chance_construct_block = c_construct_block
        self.chance_construct_box = c_construct_box

    def interact(self):
        next_pos = self.get_next_position()
        if self.is_valid(next_pos):
            rand = random.uniform(0,1)
            accumulator = 0 + self.chance_construct_block
            if rand <= accumulator:
                print('CONSTRUCT BLOCK')
                self.construct_block(next_pos)
                return
            accumulator += self.chance_construct_box
            if rand <= accumulator:
                print('CONSTRUCT BOX')
                self.construct_box(next_pos)
                return

    def construct_block(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.LIMIT_BLOCK

    def construct_box(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.BOX_BLOCK
