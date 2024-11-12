import random
from scripts.artificial_agents.chance import Chance
from scripts.artificial_agents.constructor_agent import ConstructorAgent
from scripts.artificial_agents.destructor_agent import DestructorAgent


class GeneticAlgorithm:
    population_size = 0
    generations = 0
    mutation_rate = 0.00
    level = None
    environment = None
    population = None

    def __init__(self, population_size, generations, mutation_rate, level, environment):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.level = level
        self.environment = environment
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            # ConstructorAgent config.
            chance1 = Chance()
            c_block = random.uniform(0, 1)
            c_box = 1 - c_block

            # DestructorAgent config.
            chance2 = Chance()
            c_destruct_block = random.uniform(0, 1)
            c_construct_goal = 1 - c_destruct_block

            population.append([[chance1, c_block, c_box], [chance2, c_destruct_block, c_construct_goal]])
        return population

    def fitness(self, individual):
        constructor_agent = ConstructorAgent(individual[0][0], self.level, self.environment, individual[0][1],
                                             individual[0][2])
        destructor_agent = DestructorAgent(individual[1][0], self.level, self.environment, individual[1][1],
                                           individual[1][2])

        constructor_fitness = constructor_agent.solve_level() * constructor_agent.number_blocks() * constructor_agent.difficulty_factor()
        destructor_fitness = destructor_agent.solve_level() * destructor_agent.number_blocks() * destructor_agent.difficulty_factor()

        total_fitness = constructor_fitness + destructor_fitness
        return total_fitness

    def select_parents(self, fitnesses):
        parents = random.choices(self.population, weights=fitnesses, k=2)
        return parents

    def crossover(self, parent1, parent2):
        child1_chance = Chance()
        child2_chance = Chance()

        for attr in ['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact']:
            setattr(child1_chance, attr, (getattr(parent1[0][0], attr) + getattr(parent2[0][0], attr)) / 2)

        c_block = (parent1[0][1] + parent2[0][1]) / 2
        c_box = 1 - c_block

        for attr in ['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact']:
            setattr(child2_chance, attr, (getattr(parent1[1][0], attr) + getattr(parent2[1][0], attr)) / 2)

        c_destruct_block = (parent1[1][1] + parent2[1][1]) / 2
        c_construct_goal = 1 - c_destruct_block

        return [[child1_chance, c_block, c_box], [child2_chance, c_destruct_block, c_construct_goal]]

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            attr = random.choice(['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact'])
            new_value = max(0, min(1, getattr(individual[0][0], attr) + random.uniform(-0.05, 0.05)))
            setattr(individual[0][0], attr, new_value)

        total = sum([individual[0][0].walk, individual[0][0].stop, individual[0][0].turn_left,
                     individual[0][0].turn_right, individual[0][0].turn_back, individual[0][0].interact])
        for attr in ['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact']:
            setattr(individual[0][0], attr, getattr(individual[0][0], attr) / total)

        if random.random() < self.mutation_rate:
            individual[0][1] = random.uniform(0, 1)
            individual[0][2] = 1 - individual[0][1]

        if random.random() < self.mutation_rate:
            attr = random.choice(['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact'])
            new_value = max(0, min(1, getattr(individual[1][0], attr) + random.uniform(-0.05, 0.05)))
            setattr(individual[1][0], attr, new_value)

        total = sum([individual[1][0].walk, individual[1][0].stop, individual[1][0].turn_left,
                     individual[1][0].turn_right, individual[1][0].turn_back, individual[1][0].interact])
        for attr in ['walk', 'stop', 'turn_left', 'turn_right', 'turn_back', 'interact']:
            setattr(individual[1][0], attr, getattr(individual[1][0], attr) / total)

        if random.random() < self.mutation_rate:
            individual[1][1] = random.uniform(0, 1)
            individual[1][2] = 1 - individual[1][1]

    def run(self):
        for generation in range(self.generations):
            fitnesses = [self.fitness(individual) for individual in self.population]

            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents(fitnesses)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            self.population = new_population

        best_individual = max(self.population, key=lambda ind: self.fitness(ind))
        return best_individual
