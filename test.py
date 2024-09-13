import arcade
import scripts.sokoplayer

# Define constants for the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sokoban Level"

# Define the size of each sprite
SPRITE_SIZE = 60
PLAYER_MOVEMENT_SPEED = 60

player_position_x = 0
player_position_y = 0

# Define the level matrix

level = [
    ['-', '-', '-', '-', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '#', '-', '-', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '#', '$', '-', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '#', '#', '#', '-', '-', '$', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-', '$', '-', '$', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['#', '#', '#', '-', '#', '-', '#', '#', '-', '#', '-', '-', '-', '#', '#', '#', '#', '#', '#'],
    ['#', '-', '-', '-', '#', '-', '#', '#', '-', '#', '#', '#', '#', '#', '-', '-', '.', '.', '#'],
    ['#', '-', '$', '-', '-', '$', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '-', '#', '#', '#', '-', '#', '@', '#', '#', '-', '-', '.', '.', '#'],
    ['-', '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-']
]

# Sprite file paths
SPRITES = {
    '#': ":resources:images/tiles/boxCrate_single.png",
    '-': ":resources:images/tiles/water.png",
    '$': ":resources:images/tiles/lockRed.png",
    '@': ":resources:images/tiles/switchGreen.png"
}

class Player:
    SPRITE_ADJUSTMENT_X = 30
    SPRITE_ADJUSTMENT_Y = 30
    x = 0
    y = 0
    sprite = None

    def __init__(self):
        self.set_player_initial_position()
        self.set_player_sprite()

    def set_player_initial_position(self):
        for i in range(len(level)):
            for j in range(len(level[0])):
                if level[i][j] == '@':
                    print('i = {a}'.format(a=i))
                    print('j = {a}'.format(a=j))
                    self.x = j
                    self.y = len(level) - i - 1
                    return True
        return False

    def set_player_sprite(self):
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5
        )
        self.update_player_position()

    def move_up(self):
        self.y += 1
        self.update_player_position()

    def move_down(self):
        self.y -= 1
        self.update_player_position()

    def move_left(self):
        self.x -= 1
        self.update_player_position()

    def move_right(self):
        self.x += 1
        self.update_player_position()

    def update_player_position(self):
        self.sprite.center_x = self.x * SPRITE_SIZE + self.SPRITE_ADJUSTMENT_X
        self.sprite.center_y = self.y * SPRITE_SIZE + self.SPRITE_ADJUSTMENT_Y


class SokobanLevel(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player()

        self.sprites = arcade.SpriteList()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key in [arcade.key.W, arcade.key.UP]:
            self.player.move_up()
        elif key in [arcade.key.S, arcade.key.DOWN]:
            self.player.move_down()
        elif key in [arcade.key.A, arcade.key.LEFT]:
            self.player.move_left()
        elif key in [arcade.key.D, arcade.key.RIGHT]:
            self.player.move_right()

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key in [arcade.key.W, arcade.key.UP] or key in [arcade.key.S, arcade.key.DOWN]:
            self.player.sprite.change_y = 0
        elif key in [arcade.key.A, arcade.key.LEFT] or key in [arcade.key.D, arcade.key.RIGHT]:
            self.player.sprite.change_x = 0

    def setup(self):
        # Load and position the sprites
        for row_index, row in enumerate(level):
            for col_index, item in enumerate(row):
                if item in SPRITES:
                    sprite = arcade.Sprite(SPRITES[item], scale=0.5)
                    sprite.center_x = col_index * SPRITE_SIZE + SPRITE_SIZE / 2
                    sprite.center_y = (len(level) - row_index - 1) * SPRITE_SIZE + SPRITE_SIZE / 2
                    self.sprites.append(sprite)


    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        self.player.sprite.draw()

    def on_update(self, delta_time):
        self.player.sprite.update()

def main():
    window = SokobanLevel()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()