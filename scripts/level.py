import arcade
from scripts.procedural_level_generator import LevelGenerator

# Sprite file paths
SPRITES = {
    '#': "sprites/wall_001.png",
    '-': "sprites/empty_001.png",
    '$': "sprites/trash_paper_001.png",
    '@': "sprites/empty_001.png",
    '%': ":resources:images/tiles/lockRed.png",
}

class LevelBlock:
    EMPTY_BLOCK = '-'
    BOX_BLOCK = '$'
    LIMIT_BLOCK = '#'
    GOAL_BLOCK = '.'
    BOX_UNDER_GOAL_BLOCK = '%'
    SPAWN_BLOCK = '@'

class Level:
    SPRITE_SIZE = None
    '''
    matrix = [
    ['-', '-', '-', '-', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '#', '-', '-', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '#', '$', '-', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '#', '#', '#', '-', '-', '$', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-', '$', '-', '$', '-', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['#', '#', '#', '-', '#', '-', '#', '#', '-', '#', '-', '-', '-', '#', '#', '#', '#', '#', '#'],
    ['#', '-', '-', '-', '#', '-', '#', '#', '-', '#', '#', '#', '#', '#', '-', '-', '.', '.', '#'],
    ['#', '-', '$', '-', '-', '$', '-', '-', '-', '-', '-', '-', '-', '-', '-', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '-', '#', '#', '#', '-', '#', '@', '#', '#', '-', '-', '.', '.', '#'],
    ['-', '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-']
]
    
    matrix = [
    ['#', '#', '#', '#', '#'],
    ['#', '-', '-', '-', '#'],
    ['#', '-', '$', '.', '#'],
    ['#', '-', '$', '.', '#'],
    ['#', '@', '-', '-', '#'],
    ['#', '#', '#', '#', '#']
    ]
    '''

    matrix = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "-", "-", "-", "-", "-", "-", "-", "-", "#"],
        ["#", "-", "@", "-", "#", "#", "-", "-", "-", "#"],
        ["#", "-", "-", "$", ".", "-", "-", "-", "-", "#"],
        ["#", "#", "#", "-", "-", "-", "#", "#", "#", "#"],
        ["#", "-", "-", "-", "$", "-", "-", "-", "-", "#"],
        ["#", "-", ".", "-", "-", ".", "-", "-", "-", "#"],
        ["#", "-", "-", "-", "-", "-", "-", "-", "-", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    sprite = None

    def __init__(self, sprite_size):
        self.SPRITE_SIZE = sprite_size
        self.update_level()
        print(len(self.matrix))
        print(len(self.matrix[0]))

    def update_level(self):
        self.sprite = arcade.SpriteList()
        for row_index, row in enumerate(self.matrix):
            for col_index, item in enumerate(row):
                if item in SPRITES:
                    sprite = arcade.Sprite(SPRITES[item], scale=.5)
                    sprite.center_x = col_index * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
                    sprite.center_y = (len(self.matrix) - row_index - 1) * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
                    self.sprite.append(sprite)

    def generate_new_level(self, height, width):
        self.matrix = [[0 for x in range(width)] for y in range(height)]

        

    def is_player_winner(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == LevelBlock.BOX_BLOCK:
                    return False
        return True

    def display_win_screen(self):
        print('PLAYER WIN')

    def change_level_block(self, pos_x, pos_y, new_character):
        self.matrix[pos_y][pos_x] = new_character