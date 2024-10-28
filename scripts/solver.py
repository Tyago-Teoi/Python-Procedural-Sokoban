import time
from scripts.player import Player

class Solver:
    level = None
    player = None
    delay = 0.0
    solution_tried = False
    was_solved = False
    movements = []

    def __init__(self, level, sprite_size, SOLVER_DELAY):
        self.level = level
        self.delay = SOLVER_DELAY
        self.player = Player(level, sprite_size)
        self.player.set_player_initial_position()
        self.player.set_player_sprite()

    def solve_level(self):
        pass

    def calculate_solution(self):
        pass

    def show_movements(self):
        while len(self.movements) != 0:
            movement = self.movements[0]

            if movement == 'u':
                self.player.move_up()
            elif movement == 'd':
                self.player.move_down()
            elif movement == 'l':
                self.player.move_left()
            elif movement == 'r':
                self.player.move_right()

            time.sleep(self.delay)
            self.movements.pop(0)