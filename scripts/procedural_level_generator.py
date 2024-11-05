MAX_ITERATIONS = 1024

class LevelGenerator:
    width, height = 0, 0
    difficulty = 0
    matrix = None

    def __init__(self, width, height, difficulty, player_params):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.player_params = player_params
        self.matrix = self.alocate_level_matrix()

    def generate_level(self):
        self.insert_level_border()

    def insert_level_border(self):
        for i in range(self.height + 2):
            self.matrix[i][0] = '#'
            self.matrix[i][self.width+1] = '#'
        for j in range(self.width + 2):
            self.matrix[0][j] = '#'
            self.matrix[self.height+1][j] = '#'

    def alocate_level_matrix(self):
        return [[0 for x in range(self.width+2)] for y in range(self.height+2)]

    def print(self):
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                print(self.matrix[i][j], end = " ")
            print()

test = LevelGenerator(10, 10, 1, None)
test.generate_level()
test.print()