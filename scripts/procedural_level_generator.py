from scripts.artificial_agents.destructor_agent import DestructorAgent
from scripts.artificial_agents.constructor_agent import ConstructorAgent
from scripts.artificial_agents.chance import Chance

MAX_ITERATIONS = 256
MAX_AGENTS = 4
INITIAL_AGENTS_NUMBER = 2

class LevelGenerator:
    width, height = 0, 0
    environment = None
    difficulty = 0
    level = None
    agents = []
    player_params = None

    def __init__(self, width, height, difficulty, player_params):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.player_params = player_params
        self.level = self.allocate_level()

    def generate_level(self):
        self.insert_level_border()
        self.initiate_agents()
        self.start_agents_generation()
        return self.level

    def insert_level_border(self):
        for i in range(self.height + 2):
            self.level[i][0] = '#'
            self.level[i][self.width+1] = '#'
        for j in range(self.width + 2):
            self.level[0][j] = '#'
            self.level[self.height+1][j] = '#'

    def initiate_agents(self):
        chance = Chance()
        chance.default_chance()
        destructor_agent = DestructorAgent(chance, self.player_params, self.level, .5, .5)
        constructor_agent = ConstructorAgent(chance, self.player_params, self.level, .6, .4)
        self.agents.append(destructor_agent)
        self.agents.append(constructor_agent)

        #for i in range(INITIAL_AGENTS_NUMBER):

    def start_agents_generation(self):
        for interaction in range(MAX_ITERATIONS):
            for i in range(len(self.agents)):
                self.agents[i].act()
            self.print()
            print()

    def allocate_level(self):
        return [['-' for _ in range(self.width + 2)] for _ in range(self.height + 2)]

    def print(self):
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                print(self.level[i][j], end = " ")
            print()

test = LevelGenerator(8, 4, 1, None)
test.generate_level()
test.print()