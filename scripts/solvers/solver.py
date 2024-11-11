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
        print(2)
        movements = self.movements.copy()
        print(3)
        self.player.set_animation(True)
        while movements:

            movement = movements[0]
            print(4)
            if movement == 'u':
                self.player.move_up()
            elif movement == 'd':
                self.player.move_down()
            elif movement == 'l':
                self.player.move_left()
            elif movement == 'r':
                self.player.move_right()
            print(5)
            #arcade.pause(self.delay)
            print(6)
            #time.sleep(self.delay)
            movements.pop(0)

        self.player.set_animation(False)


