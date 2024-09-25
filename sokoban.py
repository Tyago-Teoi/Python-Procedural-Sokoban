import arcade
from scripts.level import Level
from scripts.player import Player

# Define constants for the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sokoban Level"

# Define the size of each sprite
SPRITE_SIZE = 60
PLAYER_MOVEMENT_SPEED = 60

player_position_x = 0
player_position_y = 0

class SokobanLevel(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.level = Level(SPRITE_SIZE)
        self.player = Player(self.level, SPRITE_SIZE)
        self.sprites = arcade.SpriteList()

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

        self.player.print_movements()

    def on_draw(self):
        arcade.start_render()
        self.level.sprite.draw()
        self.player.sprite.draw()

    def on_update(self, delta_time):
        if self.level.is_player_winner():
            self.level.display_win_screen()
            #self.level.generate_new_level()
            pass
        self.level.update_level()
        self.player.sprite.update()

def main():
    window = SokobanLevel()
    arcade.run()

if __name__ == "__main__":
    main()