from scripts.agent import Agent
import random

class ConstructorAgent(Agent):

    chance_construct_block = 0.0
    chance_construct_box = 0.0

    def __init__(self, chance, c_construct_block, c_construct_box):
        super().__init__(chance)
        self.construct_block = c_construct_block
        self.construct_box = c_construct_box

    def interact(self):
        rand = random.uniform(0,1)

        if rand < self.chance.

        self.construct_block