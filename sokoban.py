import arcade
from scripts.level import Level
from scripts.player import Player
from scripts.solver_bfs import BFSSolver

# Define constants for the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sokoban Level"

# Solver delay constant
SOLVER_DELAY = 2

# Define the size of each sprite
SPRITE_SIZE = 64
PLAYER_MOVEMENT_SPEED = 60

player_position_x = 0
player_position_y = 0

class SokobanLevel(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.total_time = 0.0
        self.level = Level(SPRITE_SIZE)
        self.player = Player(self.level, SPRITE_SIZE)
        self.sprites = arcade.SpriteList()
        self.solver = BFSSolver(self.player, self.level, SPRITE_SIZE, SOLVER_DELAY)

    def on_key_press(self, key, modifiers):
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
        #elif key in [arcade.key.P]:
        #    self.solver.solve_level()
        #    self.player.reload_level()

        self.player.print_player_params()
        #self.player.print_movements()

    def on_draw(self):
        arcade.start_render()
        self.level.sprite.draw()
        self.player.sprite.draw()

    def on_update(self, delta_time):
        self.total_time += delta_time

        if self.level.is_player_winner():
            self.level.display_win_screen()
            #self.level.generate_new_level(self.player.player_params, self.total_time % 60)
            pass
        self.level.update_level()
        self.player.sprite.update()

def main():
    window = SokobanLevel()
    arcade.run()

if __name__ == "__main__":
    main()