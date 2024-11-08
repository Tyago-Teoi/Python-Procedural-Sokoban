from scripts.artificial_agents.agent import Agent


class DestructorAgent(Agent):
    level = None
    chance_destruct_block = 0.0

    def __init__(self, chance, player_params, level, chance_destruct_block):
        super().__init__(chance, player_params)
        self.chance_destruct_block = chance_destruct_block
        self.level = level

    def interact(self):
        self.destroy_block()

    def destroy_block(self):
        pass
