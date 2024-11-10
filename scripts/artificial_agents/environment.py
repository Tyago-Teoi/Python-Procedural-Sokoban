class Environment:
    level = None
    player_params = None
    difficulty = 1
    n_box = 0
    n_goal = 0

    def __init__(self, level, difficulty, player_params):
        self.level = level
        self.difficulty = difficulty
        self.player_params = player_params

    def add_box(self):
        self.n_box += 1

    def add_goal(self):
        self.n_goal += 1

    def sub_box(self):
        self.n_box -= 1

    def sub_goal(self):
        self.n_goal -= 1