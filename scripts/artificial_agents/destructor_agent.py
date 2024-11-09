import random
from scripts.artificial_agents.agent import Agent
from scripts.level import LevelBlock


class DestructorAgent(Agent):
    chance_destruct_block = 0.0

    def __init__(self, chance, player_params, level, chance_destruct_block):
        super().__init__(chance, level, player_params)
        self.chance_destruct_block = chance_destruct_block

    def interact(self):
        next_pos = self.get_next_position()
        if self.is_valid(next_pos):

            self.destroy_block(next_pos)

    def destroy_block(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.EMPTY_BLOCK