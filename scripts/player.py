import arcade

class Position:
    x = -1
    y = -1
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update(self, x, y):
        self.x = x
        self.y = y
    def translate_to_matrix_position(self, matrix):
        return Position(self.x, len(matrix) - self.y - 1)
    def print(self):
        print('X = {a} \t Y = {b}'.format(a=self.x, b=self.y))

class Player:
    SPRITE_SIZE = 0
    SPRITE_ADJUSTMENT_X = 30
    SPRITE_ADJUSTMENT_Y = 40

    player_movements = []
    level = None
    position = Position(0,0)
    sprite = None

    asdf= 0
    asd = 0

    def __init__(self, level, sprite_size):
        self.level = level
        self.SPRITE_SIZE = sprite_size
        self.set_player_initial_position()
        self.set_player_sprite()

    def set_player_initial_position(self):
        for i in range(len(self.level.matrix)):
            for j in range(len(self.level.matrix[0])):
                if self.level.matrix[i][j] == '@':
                    self.position.update(j, len(self.level.matrix) - i - 1)
                    return True
        return False

    def set_player_sprite(self):
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5
        )
        self.update_player_sprite_position()

    def move_up(self):
        next_position = Position(self.position.x, self.position.y + 1)
        after_next_position = Position(self.position.x, self.position.y + 2)
        self.move_execute(next_position, after_next_position, 'u', 'U')

    def move_down(self):
        next_position = Position(self.position.x, self.position.y - 1)
        after_next_position = Position(self.position.x, self.position.y - 2)
        self.move_execute(next_position, after_next_position, 'd', 'D')

    def move_left(self):
        next_position = Position(self.position.x - 1, self.position.y)
        after_next_position = Position(self.position.x - 2, self.position.y)
        self.move_execute(next_position, after_next_position, 'l', 'L')

    def move_right(self):
        next_position = Position(self.position.x + 1, self.position.y)
        after_next_position = Position(self.position.x + 2, self.position.y)
        self.move_execute(next_position, after_next_position, 'r', 'R')

    def move_execute(self, next_position, after_next_position, move_character_minor, move_character_major):
        translated_position = next_position.translate_to_matrix_position(self.level.matrix)
        translated_next_position = after_next_position.translate_to_matrix_position(self.level.matrix)
        next_pos_char = self.level.matrix[translated_position.y][translated_position.x]
        after_next_pos_char = self.level.matrix[translated_next_position.y][translated_next_position.x]

        if next_pos_char == '-' or next_pos_char == '.' or next_pos_char == '@':
            self.end_move_execute(next_position, move_character_minor)
        elif next_pos_char == '$'  and after_next_pos_char == '-':
            self.update_level_on_block_push(translated_position, translated_next_position, '-', '$')
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == '$' and after_next_pos_char == '.':
            self.update_level_on_block_push(translated_position, translated_next_position, '-', '%')
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == '%' and after_next_pos_char == '.':
            self.update_level_on_block_push(translated_position, translated_next_position, '.', '%')
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == '%' and after_next_pos_char == '-':
            self.update_level_on_block_push(translated_position, translated_next_position, '.', '$')
            self.end_move_execute(next_position, move_character_major)

    def end_move_execute(self, next_position, move_character):
        self.set_player_position(next_position)
        self.player_movements.append(move_character)

    def update_level_on_block_push(self, translated_next_pos, translated_after_next_pos, next_char, after_next_char):
        self.level.change_level_block(translated_next_pos.x, translated_next_pos.y, next_char)
        self.level.change_level_block(translated_after_next_pos.x, translated_after_next_pos.y, after_next_char)

    def set_player_position(self, next_position):
        self.position.update(next_position.x, next_position.y)
        self.update_player_sprite_position()

    def update_player_sprite_position(self):
        self.sprite.center_x = self.position.x * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_X
        self.sprite.center_y = self.position.y * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_Y