import random
from scripts.artificial_agents.agent import Agent
from scripts.level import LevelBlock

class ConstructorAgent(Agent):
    level = None
    chance_construct_block = 0.0
    chance_construct_box = 0.0

    def __init__(self, chance, player_params, level, c_construct_block, c_construct_box):
        super().__init__(chance, player_params)
        self.construct_block = c_construct_block
        self.construct_box = c_construct_box
        self.level = level

    def interact(self):
        next_pos = self.get_next_position()
        if self.is_valid(next_pos):
            rand = random.uniform(0,1)
            accumulator = 0 + self.chance_construct_block
            if rand < accumulator:
                self.construct_block(next_pos)
            accumulator += self.chance_construct_box
            if rand < accumulator:
                self.construct_box(next_pos)

    def construct_block(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.LIMIT_BLOCK

    def construct_box(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.BOX_BLOCK