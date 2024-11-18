from scripts.utils.timer import Timer
import random

HEIGHT_PERCENTAGE_MOD = 0.1
WIDTH_PERCENTAGE_MOD = 0.3

TIME_MOD_WEIGHT = 1
PLAYER_MOVE_WEIGHT = 1

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 10

MIN_DIFFICULTY_ADJUSTMENT = -2
MAX_DIFFICULTY_ADJUSTMENT = 2
TIME_FACTOR_RATIO_DIFFERENCE = .5

MOVE_WEIGHT = 1
RESET_WEIGHT = 3
REDO_WEIGHT = 1.5
VICTORY_WEIGHT = 1
MOVE_FACTOR_RATIO_DIFFERENCE = 5 #Always >= 1

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

    def update(self, player_params, solver_movements, timer: Timer):
        # [-2, +2] game difficulty adjustment
        f_time = self.time_modification_factor(timer.level_time)
        f_move = self.player_movement_modification_factor(player_params, solver_movements)

        difficulty_modification_factor = ((TIME_MOD_WEIGHT * f_time + PLAYER_MOVE_WEIGHT * f_move) /
                                          (TIME_MOD_WEIGHT + PLAYER_MOVE_WEIGHT))

        print('f_time: {a} \t f_move: {b}'.format(a=f_time, b=f_move))
        print('difficulty_modification_factor: {a}'.format(a=difficulty_modification_factor))

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
        return normalize_difficulty_factor(ratio, 1-TIME_FACTOR_RATIO_DIFFERENCE, 1+TIME_FACTOR_RATIO_DIFFERENCE)

    def player_movement_modification_factor(self, player_params, solver_movements) -> float:
        n_movements_to_win = len(solver_movements)
        n_moves = player_params['n_moves']
        n_resets = player_params['n_resets']
        n_redos = player_params['n_redos']

        sum_player_iterations = n_moves * MOVE_WEIGHT + n_resets * RESET_WEIGHT + n_redos * REDO_WEIGHT
        if sum_player_iterations <= n_movements_to_win:
            return MAX_DIFFICULTY_ADJUSTMENT
        if sum_player_iterations >= n_movements_to_win * MOVE_FACTOR_RATIO_DIFFERENCE:
            return MIN_DIFFICULTY_ADJUSTMENT
        return normalize_difficulty_factor(sum_player_iterations, n_movements_to_win, n_movements_to_win * MOVE_FACTOR_RATIO_DIFFERENCE)

    def update_level_dimensions(self):
        # 1 -> 3x3=9, 2 -> 5x5=25, 3 -> 6x6=36
        self.height = 3 + random.randint(round(self.difficulty), round(self.difficulty + self.difficulty * HEIGHT_PERCENTAGE_MOD))
        self.width = 3 + random.randint(round(self.difficulty), round(self.difficulty + self.difficulty * WIDTH_PERCENTAGE_MOD))

    def add_box(self):
        self.n_box += 1

    def add_goal(self):
        self.n_goal += 1

    def sub_box(self):
        self.n_box -= 1

    def sub_goal(self):
        self.n_goal -= 1

    def print(self):
        print('ENVIRONMENT')
        print('(height, width) = ({a}, {b})'.format(a=self.height, b=self.width))
        print('difficulty = {a}'.format(a=self.difficulty))
        print('player params:')
        print(self.player_params)

        height, width = 0, 0
        player_params = None
        difficulty = 1
        n_box = 0
        n_goal = 0
        print()

# normalization of ratio between min and max difficulty adjustments
def normalize_difficulty_factor(ratio, min_limit_ratio, max_limit_ratio):
    return -1*(MIN_DIFFICULTY_ADJUSTMENT + (MAX_DIFFICULTY_ADJUSTMENT - MIN_DIFFICULTY_ADJUSTMENT) *
               (ratio - min_limit_ratio) / (max_limit_ratio - min_limit_ratio))

def test():
    player_params = {
        'n_moves': 24,
        'n_resets': 0,
        'n_redos': 0,
        'n_solver_uses': 0,
        'n_victories': 0
    }
    moves = ['u', 'l', 'l', 'd', 'r']
    timer = Timer()
    timer.on_update(1.49)
    env = Environment(height=1, width=1, difficulty=1, player_params=player_params)
    env.update(player_params, moves, timer)

#test()