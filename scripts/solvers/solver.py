class Solver:
    timer = None
    level = None
    player = None
    delay = 0
    solution_tried = False
    was_solved = False
    path = []
    movements = []

    def __init__(self, player, level, timer, SOLVER_DELAY):
        self.level = level
        self.delay = SOLVER_DELAY
        self.player = player
        self.timer = timer

    def solve_level(self):
        pass

    def calculate_solution(self):
        pass

    def move_solver(self):
        #self.player.reload_level()
        movement = self.movements[0]
        print(movement)

        if movement == 'u':
            self.player.move_up()
        elif movement == 'd':
            self.player.move_down()
        elif movement == 'l':
            self.player.move_left()
        elif movement == 'r':
            self.player.move_right()

        self.movements.pop(0)
        return len(self.movements)

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

            movements.pop(0)




