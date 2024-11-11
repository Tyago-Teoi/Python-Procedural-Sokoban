import arcade
from scripts.level import Level
from scripts.player import Player
from scripts.solvers.solver_bfs import BFSSolver
from scripts.utils.timer import Timer

# Define constants for the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sokoban Level"

# Solver delay constant
SOLVER_DELAY = 1.5

# Define the size of each sprite
SPRITE_SIZE = 64
PLAYER_MOVEMENT_SPEED = 60

player_position_x = 0
player_position_y = 0

is_solving = False
count = 0

class SokobanLevel(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.timer = Timer()
        self.level = Level(SPRITE_SIZE)
        self.player = Player(self.level, SPRITE_SIZE)
        self.sprites = arcade.SpriteList()
        self.solver = BFSSolver(self.player, self.level, self.timer, SOLVER_DELAY)

    def on_key_press(self, key, modifiers):
        global is_solving
        if not is_solving:
            # MOVE KEYS
            if key in [arcade.key.W, arcade.key.UP]:
                self.player.move_up()
            elif key in [arcade.key.S, arcade.key.DOWN]:
                self.player.move_down()
            elif key in [arcade.key.A, arcade.key.LEFT]:
                self.player.move_left()
            elif key in [arcade.key.D, arcade.key.RIGHT]:
                self.player.move_right()

            # RE-DO KEY
            elif key in [arcade.key.R]:
                self.player.move_redo()

            # RELOAD LEVEL KEY
            elif key in [arcade.key.ESCAPE]:
                self.player.reload_level()

            # SOLVE LEVEL BY SOLVER
            elif key in [arcade.key.P]:
                is_solving = True
                self.player.reload_level()
                #self.player.reload_level()

            self.player.print_player_params()
            #self.player.print_movements()

    def on_draw(self):
        arcade.start_render()
        self.level.sprite.draw()
        self.player.sprite.draw()

    def on_update(self, delta_time):
        global is_solving
        global count
        count += 1
        if self.level.is_player_winner():
            self.level.display_win_screen()
            print("WIN")
            pass
        if is_solving and count%2 == 0:
            arcade.pause(SOLVER_DELAY)
            solver_movements_remaining = self.solver.move_solver()
            if solver_movements_remaining <= 0:
                is_solving = False
                count = 0

        self.level.update_level()
        self.player.sprite.update()


def main():
    window = SokobanLevel()
    arcade.run()

if __name__ == "__main__":
    main()