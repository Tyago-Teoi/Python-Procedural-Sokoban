import random
from scripts.artificial_agents.agent import Agent
from scripts.level import LevelBlock


class DestructorAgent(Agent):
    name = "Destructor"
    chance_destruct_block = 0.0
    chance_construct_goal = 0.0

    def __init__(self, chance, level, environment, c_destruct_block, c_construct_goal):
        super().__init__(chance, level, environment)
        self.chance_destruct_block = c_destruct_block
        self.chance_construct_goal = c_construct_goal

    def interact(self):
        next_pos = self.get_next_position()
        if self.is_valid(next_pos):
            rand = random.uniform(0, 1)
            accumulator = 0 + self.chance_destruct_block
            if rand <= accumulator:
                self.destroy_block(next_pos)
                return
            accumulator += self.chance_construct_goal
            if rand <= accumulator:
                self.construct_goal(next_pos)
                return

    def destroy_block(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.EMPTY_BLOCK

    def construct_goal(self, next_pos):
        self.level[next_pos.y][next_pos.x] = LevelBlock.GOAL_BLOCK