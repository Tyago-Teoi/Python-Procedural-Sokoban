import arcade

# Define constants for the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sokoban Level"

# Define the size of each sprite
SPRITE_SIZE = 60
PLAYER_MOVEMENT_SPEED = 5

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

class SokobanLevel(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.sprites = arcade.SpriteList()
        self.player_sprite = None

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key in [arcade.key.W, arcade.key.UP]:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key in [arcade.key.S, arcade.key.DOWN]:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key in [arcade.key.A, arcade.key.LEFT]:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key in [arcade.key.D, arcade.key.RIGHT]:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key in [arcade.key.W, arcade.key.UP] or key in [arcade.key.S, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        elif key in [arcade.key.A, arcade.key.LEFT] or key in [arcade.key.D, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0

    def setup(self):
        # Load and position the sprites
        for row_index, row in enumerate(level):
            for col_index, item in enumerate(row):
                if item in SPRITES:
                    sprite = arcade.Sprite(SPRITES[item], scale=0.5)
                    sprite.center_x = col_index * SPRITE_SIZE + SPRITE_SIZE / 2
                    sprite.center_y = (len(level) - row_index - 1) * SPRITE_SIZE + SPRITE_SIZE / 2
                    self.sprites.append(sprite)

        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5
        )

        # Set the player's initial position
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        self.player_sprite.draw()

    def on_update(self, delta_time):
        self.player_sprite.update()

def main():
    window = SokobanLevel()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()