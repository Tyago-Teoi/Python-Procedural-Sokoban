from scripts.utils.timer import Timer
import random

TIME_MOD_WEIGHT = 1
PLAYER_MOVE_WEIGHT = 1
MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 10

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
        difficulty_modification_factor = ((TIME_MOD_WEIGHT * self.time_modification_factor(timer.level_time) +
                                          PLAYER_MOVE_WEIGHT * self.player_movement_modification_factor(player_params)) /
                                          (TIME_MOD_WEIGHT+PLAYER_MOVE_WEIGHT))

        self.difficulty += difficulty_modification_factor
        if round(self.difficulty) < MIN_DIFFICULTY:
            self.difficulty = MIN_DIFFICULTY
        elif round(self.difficulty) > MAX_DIFFICULTY:
            self.difficulty = MAX_DIFFICULTY

        self.update_level_dimensions()

    def time_modification_factor(self, level_time: float) -> float:
        pass

    def player_movement_modification_factor(self, player_params) -> float:
        pass

    def update_level_dimensions(self):
        # 1 -> 3x3=9, 2 -> 5x5=25, 3 -> 6x6=36
        self.height = 3 + random.randint(self.difficulty, round(self.difficulty * 0.1))
        self.width = 3 + random.randint(self.difficulty, round(self.difficulty * 0.3))

    def add_box(self):
        self.n_box += 1

    def add_goal(self):
        self.n_goal += 1

    def sub_box(self):
        self.n_box -= 1

    def sub_goal(self):
        self.n_goal -= 1
