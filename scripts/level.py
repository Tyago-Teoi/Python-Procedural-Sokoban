import arcade
# Sprite file paths
SPRITES = {
    '#': ":resources:images/tiles/boxCrate_single.png",
    '-': ":resources:images/tiles/water.png",
    '$': ":resources:images/tiles/lockRed.png",
    '@': ":resources:images/tiles/switchGreen.png"
}

class Level:

    SPRITE_SIZE = None

    matrix = [
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
    sprite = None

    def __init__(self, sprite_size):
        self.SPRITE_SIZE = sprite_size
        self.update_level()

    def update_level(self):

        self.sprite = arcade.SpriteList()

        for row_index, row in enumerate(self.matrix):
            for col_index, item in enumerate(row):
                if item in SPRITES:
                    sprite = arcade.Sprite(SPRITES[item], scale=0.5)
                    sprite.center_x = col_index * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
                    sprite.center_y = (len(self.matrix) - row_index - 1) * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
                    self.sprite.append(sprite)

        #self.sprite.update()