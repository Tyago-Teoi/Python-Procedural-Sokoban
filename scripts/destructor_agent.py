from scripts.agent import Agent
import random

class DestructorAgent(Agent):
    level = None
    chance_destruct_block = 0.0

    def __init__(self, chance, level, chance_destruct_block):
        super().__init__(chance)
        self.chance_destruct_block = chance_destruct_block
        self.level = level

    def interact(self):
        self.destroy_block()

    def destroy_block(self):
        pass
