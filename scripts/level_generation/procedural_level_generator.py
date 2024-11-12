from scripts.artificial_agents.destructor_agent import DestructorAgent
from scripts.artificial_agents.constructor_agent import ConstructorAgent
from scripts.artificial_agents.chance import Chance
from scripts.artificial_agents.environment import Environment
from scripts.level_generation.manual_levels import ManualLevel

MAX_ITERATIONS = 256
MAX_AGENTS = 4
INITIAL_AGENTS_NUMBER = 2

class LevelGenerator:
    environment = None
    level = None
    agents = []

    def __init__(self, environment):
        self.environment = environment
        self.level = self.allocate_level()

    def generate_level(self):
        level_difficulty = self.environment.difficulty
        if int(level_difficulty) == 1 or int(level_difficulty) == 2:
            temp = self.environment.player_params
            self.level, self.environment = ManualLevel(level_difficulty).select_level()
            self.environment.player_params = temp
        else:
            self.insert_level_border()
            self.initiate_agents()
            self.start_agents_generation()

        return self.level

    def insert_level_border(self):
        for i in range(self.environment.height + 2):
            self.level[i][0] = '#'
            self.level[i][self.environment.width+1] = '#'
        for j in range(self.environment.width + 2):
            self.level[0][j] = '#'
            self.level[self.environment.height+1][j] = '#'

    def initiate_agents(self):
        chance = Chance()
        chance.default_chance()
        destructor_agent = DestructorAgent(chance, self.level, self.environment, .5, .5)
        constructor_agent = ConstructorAgent(chance, self.level, self.environment, .6, .4)
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
        return [['-' for _ in range(self.environment.width + 2)] for _ in range(self.environment.height + 2)]

    def print(self):
        for i in range(self.environment.height + 2):
            for j in range(self.environment.width + 2):
                print(self.level[i][j], end = " ")
            print()

def t():
    environment = Environment(4, 8, 1, None)
    test = LevelGenerator(environment)
    test.generate_level()
    test.print()

t()