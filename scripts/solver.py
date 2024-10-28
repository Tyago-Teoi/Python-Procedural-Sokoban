import arcade
from scripts.player import Player

class Solver:
    level = None
    player = None
    delay = 0
    solution_tried = False
    was_solved = False
    path = []
    movements = []

    def __init__(self, player, level, sprite_size, SOLVER_DELAY):
        self.level = level
        self.delay = SOLVER_DELAY
        self.player = player

    def solve_level(self):
        pass

    def calculate_solution(self):
        pass

    def show_movements(self):
        self.player.reload_level()
        movements = self.movements.copy()
        while movements:
            movement = movements[0]

            if movement == 'u':
                self.player.move_up()
            elif movement == 'd':
                self.player.move_down()
            elif movement == 'l':
                self.player.move_left()
            elif movement == 'r':
                self.player.move_right()

            arcade.pause(self.delay)
            #time.sleep(self.delay)
            movements.pop(0)

