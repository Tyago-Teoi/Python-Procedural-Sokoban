from scripts.agent import Agent
import random

class DestructorAgent(Agent):
    level = None
    def __init__(self, chance, level):
        super().__init__(chance)
        self.level = level

    def interact(self):
        self.destroy_block()

    def destroy_block(self):
        pass
