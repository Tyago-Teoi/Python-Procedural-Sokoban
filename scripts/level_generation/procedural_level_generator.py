from scripts.artificial_agents.destructor_agent import DestructorAgent
from scripts.artificial_agents.constructor_agent import ConstructorAgent
from scripts.level_generation.level import Level
from scripts.artificial_agents.chance import Chance
from scripts.artificial_agents.environment import Environment
from scripts.artificial_agents.genetic_algorithm import GeneticAlgorithm
from scripts.level_generation.manual_levels import ManualLevel

MAX_ITERATIONS = 256

class LevelGenerator:
    sprite_size = 0
    environment = None
    level = None
    agents = []

    def __init__(self, SPRITE_SIZE, environment):
        self.sprite_size = SPRITE_SIZE
        self.environment = environment
        self.level = self.allocate_level()

    def generate_next_level(self, player_params, solver_movements, timer):
        self.environment.update(player_params, solver_movements, timer)
        self.generate_level()

    def generate_level(self):
        level_difficulty = self.environment.difficulty
        if round(level_difficulty) == 1 or round(level_difficulty) == 2:
            temp = self.environment.player_params
            self.level, self.environment = ManualLevel(level_difficulty).select_level()
            self.environment.player_params = temp
        else:
            self.insert_level_border()
            self.start_agents_generation()

        return Level(self.sprite_size, self.level)

    def insert_level_border(self):
        for i in range(self.environment.height + 2):
            self.level[i][0] = '#'
            self.level[i][self.environment.width+1] = '#'
        for j in range(self.environment.width + 2):
            self.level[0][j] = '#'
            self.level[self.environment.height+1][j] = '#'


    def start_agents_generation(self):
        blank_level = self.level.copy()
        genetic_algo = GeneticAlgorithm(10, 10, .05, blank_level, self.environment)
        best_individual = genetic_algo.run()
        print(best_individual)
        #self.level =

    def generate_level_by_agent_actions(self, agents):
        for interaction in range(MAX_ITERATIONS):
            for i in range(len(agents)):
                agents[i].act()

    def allocate_level(self):
        return [['-' for _ in range(self.environment.width + 2)] for _ in range(self.environment.height + 2)]


    def print(self):
        for i in range(self.environment.height + 2):
            for j in range(self.environment.width + 2):
                print(self.level[i][j], end = " ")
            print()

def t():
    environment = Environment(6, 6, 3, None)
    test = LevelGenerator(64,environment)
    test.generate_level()
    test.print()

#t()