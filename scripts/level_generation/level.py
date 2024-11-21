import arcade
import random
#from scripts.procedural_level_generator import LevelGenerator

# Sprite file paths
SPRITES = {
    '#': "sprites/wall_001.png",
    '-': "sprites/empty_001.png",
    '$': {'plastic':["sprites/trash_plastic_001.png",
                     "sprites/trash_plastic_002.png"],
          'metal':["sprites/trash_metal_001.png",
                     "sprites/trash_metal_002.png"],
          'paper':["sprites/trash_paper_001.png",
                     "sprites/trash_paper_002.png"],
          'glass':["sprites/trash_glass_001.png",
                     "sprites/trash_glass_002.png"],
          'generic':["sprites/trash_glass_001.png",
                     "sprites/trash_paper_002.png"]},
    '@': "sprites/empty_001.png",
    '%': {'plastic':"sprites/can_plastic_002.png",
          'metal': 'sprites/can_metal_002.png',
          'paper': 'sprites/can_paper_002.png',
          'glass': 'sprites/can_glass_002.png',
          'generic': 'sprites/can_generic_002.png'},
    '.': {'plastic':"sprites/can_plastic_001.png",
          'metal': 'sprites/can_metal_001.png',
          'paper': 'sprites/can_paper_001.png',
          'glass': 'sprites/can_glass_001.png',
          'generic': 'sprites/can_generic_001.png'}
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
    '''
    matrix = None
    sprite = None
    trash_type = 'generic'
    trash_index = -1

    def __init__(self, sprite_size, matrix, trash_type):
        self.trash_type = trash_type
        self.SPRITE_SIZE = sprite_size
        self.matrix = matrix
        self.update_level()

    def update_level(self):
        self.sprite = arcade.SpriteList()
        for row_index, row in enumerate(self.matrix):
            for col_index, item in enumerate(row):
                if item in SPRITES:
                    if item == LevelBlock.BOX_BLOCK:
                        if self.trash_index == -1:
                            self.trash_index = random.randint(0, len(SPRITES[item][self.trash_type]) - 1)
                        self.setup_sprite(SPRITES[item][self.trash_type][self.trash_index], col_index, row_index)
                    elif item == LevelBlock.GOAL_BLOCK or item == LevelBlock.BOX_UNDER_GOAL_BLOCK :
                        self.setup_sprite(SPRITES[item][self.trash_type], col_index, row_index)
                    else:
                        self.setup_sprite(SPRITES[item],  col_index, row_index)

    def setup_sprite(self, sprite_path, col_index, row_index):
        sprite = arcade.Sprite(sprite_path, scale=1)
        sprite.center_x = col_index * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
        sprite.center_y = (len(self.matrix) - row_index - 1) * self.SPRITE_SIZE + self.SPRITE_SIZE / 2
        self.sprite.append(sprite)

    def generate_new_level(self, height, width):
        self.matrix = [['-' for x in range(width)] for y in range(height)]

    def is_player_winner(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == LevelBlock.BOX_BLOCK:
                    return False
        return True

    def count_blocks(self):
        boxes = 0
        goals = 0
        empties = 0
        limits = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == LevelBlock.BOX_BLOCK:
                    boxes += 1
                if self.matrix[i][j] == LevelBlock.LIMIT_BLOCK:
                    limits += 1
                if self.matrix[i][j] == LevelBlock.EMPTY_BLOCK:
                    empties += 1
                if self.matrix[i][j] == LevelBlock.GOAL_BLOCK:
                    goals += 1
        return boxes, empties, goals, limits

    def display_win_screen(self):
        #print('PLAYER WIN')
        pass

    def change_level_block(self, pos_x, pos_y, new_character):
        self.matrix[pos_y][pos_x] = new_character

