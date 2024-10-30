from scripts.agent import Agent
import random

class ConstructorAgent(Agent):
    level = None
    chance_construct_block = 0.0
    chance_construct_box = 0.0

    def __init__(self, chance, level, c_construct_block, c_construct_box):
        super().__init__(chance)
        self.construct_block = c_construct_block
        self.construct_box = c_construct_box
        self.level = level

    def interact(self):
        rand = random.uniform(0,1)
        accumulator = 0 + self.chance_construct_block

        if rand < accumulator:
            self.construct_block()
        accumulator += self.chance_construct_box
        if rand < accumulator:
            self.construct_box()

    def construct_block(self):
        pass

    def construct_box(self):
        pass