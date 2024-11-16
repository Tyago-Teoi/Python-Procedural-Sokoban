from scripts.utils.timer import Timer
import random

TIME_MOD_WEIGHT = 1
PLAYER_MOVE_WEIGHT = 1

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 10

MIN_DIFFICULTY_ADJUSTMENT = -2
MAX_DIFFICULTY_ADJUSTMENT = 2
TIME_FACTOR_RATIO_DIFFERENCE = 0.5

ARBITRARY_SECONDS_PER_MOVE = 1

class Environment:
    height, width = 0, 0
    player_params = None
    difficulty = 1
    n_box = 0
    n_goal = 0

    def __init__(self, height: int, width: int, difficulty: int, player_params: dict):
        self.height = height
        self.width = width
        self.difficulty = difficulty
        self.player_params = player_params

    def update_environment(self, player_params, timer: Timer):
        difficulty_modification_factor = 0.0

        # [-2, +2] game difficulty adjustment
        f_time = self.time_modification_factor(timer.level_time)
        f_move = self.player_movement_modification_factor(player_params)

        difficulty_modification_factor = ((TIME_MOD_WEIGHT * f_time + PLAYER_MOVE_WEIGHT * f_move) /
                                          (TIME_MOD_WEIGHT + PLAYER_MOVE_WEIGHT))

        print('f_time: {a} \t f_move: {b}'.format(a=f_time, b=f_move))

        self.difficulty += difficulty_modification_factor
        if round(self.difficulty) < MIN_DIFFICULTY:
            self.difficulty = MIN_DIFFICULTY
        elif round(self.difficulty) > MAX_DIFFICULTY:
            self.difficulty = MAX_DIFFICULTY

        self.update_level_dimensions()

    def time_modification_factor(self, level_time: float) -> float:
        level_area = self.height * self.width
        ratio = level_time / (level_area * ARBITRARY_SECONDS_PER_MOVE)

        if ratio <= (1 - TIME_FACTOR_RATIO_DIFFERENCE):
            return MAX_DIFFICULTY_ADJUSTMENT
        if ratio >= (1 + TIME_FACTOR_RATIO_DIFFERENCE):
            return MIN_DIFFICULTY_ADJUSTMENT
        # normalization of ratio between min and max difficulty adjustments
        return -1*(MIN_DIFFICULTY_ADJUSTMENT + (MAX_DIFFICULTY_ADJUSTMENT - MIN_DIFFICULTY_ADJUSTMENT) * (ratio - (1 - TIME_FACTOR_RATIO_DIFFERENCE))/(2*TIME_FACTOR_RATIO_DIFFERENCE))

    def player_movement_modification_factor(self, player_params) -> float:
        return -999
        pass

    def update_level_dimensions(self):
        # 1 -> 3x3=9, 2 -> 5x5=25, 3 -> 6x6=36
        self.height = 3 + random.randint(self.difficulty, round(self.difficulty + self.difficulty * 0.1))
        self.width = 3 + random.randint(self.difficulty, round(self.difficulty + self.difficulty * 0.3))

    def add_box(self):
        self.n_box += 1

    def add_goal(self):
        self.n_goal += 1

    def sub_box(self):
        self.n_box -= 1

    def sub_goal(self):
        self.n_goal -= 1

def test():
    player_params = {
        'n_moves': 0,
        'n_resets': 0,
        'n_redos': 0,
        'n_solver_uses': 0,
        'n_victories': 0
    }
    env = Environment(height=1, width=1, difficulty=1, player_params=player_params)
    timer = Timer()
    timer.on_update(1.49)
    env.update_environment(player_params, timer)

test()

