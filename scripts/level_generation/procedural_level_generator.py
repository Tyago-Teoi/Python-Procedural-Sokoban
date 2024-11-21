import copy
from scripts.artificial_agents.destructor_agent import DestructorAgent
from scripts.artificial_agents.constructor_agent import ConstructorAgent
from scripts.level_generation.level import Level
from scripts.artificial_agents.chance import Chance
from scripts.artificial_agents.environment import Environment, MAX_DIFFICULTY
from scripts.artificial_agents.genetic_algorithm import GeneticAlgorithm
from scripts.level_generation.manual_levels import ManualLevel
from scripts.utils.timer import Timer
from scripts.solvers.solver_bfs import BFSSolver
from scripts.level_generation.player import Player

MAX_ITERATIONS = 256
POPULATION_SIZE = 10
GENERATIONS = 10

class LevelGenerator:
    n_agents_iterations = MAX_ITERATIONS
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
        return self.generate_level()

    def generate_level(self):
        level_difficulty = self.environment.difficulty
        if round(level_difficulty) == 1 or round(level_difficulty) == 2 or round(level_difficulty) == 3:
            self.level, self.environment = ManualLevel(level_difficulty).select_level()
        else:
            self.update_max_iterations()
            self.level = self.allocate_level()
            self.insert_level_border()
            self.start_agents_generation()
        return Level(self.sprite_size, self.level, self.environment.trash_type)

    def insert_level_border(self):
        for i in range(self.environment.height + 2):
            self.level[i][0] = '#'
            self.level[i][self.environment.width+1] = '#'
        for j in range(self.environment.width + 2):
            self.level[0][j] = '#'
            self.level[self.environment.height+1][j] = '#'

    def start_agents_generation(self):
        count = 0
        solver_return = False
        new_level = None
        agent_chances = self.get_agents_chances()
        # self.print_best_agent_chances(agent_chances)
        while count <= 100 and solver_return is False:
            count+=1
            new_level = copy.deepcopy(self.level)
            self.update_agent_list(agent_chances, new_level)
            self.generate_level_by_agent_actions(self.agents)
            solver_return = self.is_level_solvable(new_level)

        if solver_return is True:
            self.level = new_level
            self.print_level(self.level)
            return
        print('NO SOLUTION FOUND SO NO LEVEL GENERATED')
        self.level, self.environment = ManualLevel(2).select_level()

    def get_agents_chances(self):
        blank_level = copy.deepcopy(self.level)
        genetic_algo = GeneticAlgorithm(POPULATION_SIZE, GENERATIONS, .05, blank_level, self.environment, self.n_agents_iterations)
        best_individual = genetic_algo.run()
        # self.print_best_agent_chances(best_individual)
        # [[constructor.chance, construct_block_chance, construct_box_chance],
        # [destructor.chance, destruct_block_chance, construct_goal_chance]]
        return best_individual

    def update_agent_list(self, agent_chances, new_level):
        constructor_agent = ConstructorAgent(agent_chances[0][0], new_level, self.environment, agent_chances[0][1], agent_chances[0][2])
        destructor_agent = DestructorAgent(agent_chances[1][0], new_level, self.environment, agent_chances[1][1], agent_chances[1][2])
        self.agents = [constructor_agent, destructor_agent]

    def generate_level_by_agent_actions(self, agents):
        for interaction in range(self.n_agents_iterations):
            for i in range(len(agents)):
                agents[i].act()

    def is_level_solvable(self, new_level):
        level_object = Level(64, copy.deepcopy(new_level), 'generic')
        player = Player(level_object, 64)
        solver = BFSSolver(player, level_object, None, None)
        return solver.solve_level()

    def allocate_level(self):
        return [['-' for _ in range(self.environment.width + 2)] for _ in range(self.environment.height + 2)]

    def update_max_iterations(self):
        self.n_agents_iterations = round(self.environment.difficulty**2 * MAX_ITERATIONS/(MAX_DIFFICULTY**2))

    def print_best_agent_chances(self, best_individual):
        print()
        print('CONSTRUCTOR AGENT')
        best_individual[0][0].print()
        print('construct block: {a}'.format(a=best_individual[0][1]))
        print('construct box: {a}'.format(a=best_individual[0][2]))
        print()
        print('DESTRUCTOR AGENT')
        best_individual[1][0].print()
        print('destruct block: {a}'.format(a=best_individual[1][1]))
        print('construct goal: {a}'.format(a=best_individual[1][2]))
        print()

    def print_level(self, level):
        for i in range(len(level)):
            print(level[i])
        print()

#put on a copy of "sprites" folder inside the "level_generation" folder
def test():
    environment = Environment(6, 6, 2, None)
    test = LevelGenerator(64,environment)

    player_params = {
        'n_moves': 0,
        'n_resets': 0,
        'n_redos': 0,
        'n_solver_uses': 0,
        'n_victories': 0
    }
    solver_moves = ['u', 'l', 'l', 'd', 'r']
    timer = Timer()
    timer.on_update(0)
    # START generate next level like
    test.environment.update(player_params, solver_moves, timer)
    test.environment.print()
    level = test.generate_level()
    # END generate next level like
    test.print()
#test()