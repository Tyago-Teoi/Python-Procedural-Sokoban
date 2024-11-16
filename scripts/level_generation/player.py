import arcade
from scripts.utils.position import Position
from scripts.level_generation.level import LevelBlock

class Player:
    is_animation = False
    SPRITE_SIZE = 0
    SPRITE_ADJUSTMENT_X = 30
    SPRITE_ADJUSTMENT_Y = 40

    player_params = {
        'n_moves': 0,
        'n_resets': 0,
        'n_redos': 0,
        'n_solver_uses': 0,
        'n_victories': 0
    }

    initial_pos = Position(0,0)
    player_movements = []
    level = None
    position = Position(0,0)
    sprite = None

    def __init__(self, level, sprite_size):
        self.level = level
        self.SPRITE_SIZE = sprite_size
        self.set_player_initial_position()

    def set_player_next_level(self, level):
        self.level = level
        self.set_player_initial_position()

    def set_player_initial_position(self):
        for i in range(len(self.level.matrix)):
            for j in range(len(self.level.matrix[0])):
                if self.level.matrix[i][j] == LevelBlock.SPAWN_BLOCK:
                    self.level.change_level_block(j, i, LevelBlock.EMPTY_BLOCK)
                    self.initial_pos.update(j, len(self.level.matrix) - i - 1)
                    self.position.update(j, len(self.level.matrix) - i - 1)
                    self.set_player_sprite()
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

    def reload_level(self):
        if len(self.player_movements) != 0:
            self.set_player_params('n_resets', 1)

        count = 0
        while len(self.player_movements):
            count += 1
            self.move_redo()

        self.set_player_params('n_redos', -count)

    def move_redo(self):
        if len(self.player_movements):
            self.set_player_params('n_redos', 1)
            move = self.player_movements.pop()

            if move == 'u':
                self.move_down()
            elif move == 'd':
                self.move_up()
            elif move == 'l':
                self.move_right()
            elif move == 'r':
                self.move_left()
            if move == 'U':
                self.set_player_position(Position(self.position.x, self.position.y + 2))
                self.move_down()
                self.set_player_position(Position(self.position.x, self.position.y - 2))
            elif move == 'D':
                self.set_player_position(Position(self.position.x, self.position.y - 2))
                self.move_up()
                self.set_player_position(Position(self.position.x, self.position.y + 2))
            elif move == 'L':
                self.set_player_position(Position(self.position.x - 2, self.position.y))
                self.move_right()
                self.set_player_position(Position(self.position.x + 2, self.position.y))
            elif move == 'R':
                self.set_player_position(Position(self.position.x + 2, self.position.y))
                self.move_left()
                self.set_player_position(Position(self.position.x - 2, self.position.y))

            self.set_player_params('n_moves', -1)
            self.player_movements.pop()

    def move_execute(self, next_position, after_next_position, move_character_minor, move_character_major):
        translated_position = next_position.translate_to_matrix_position(self.level.matrix)
        translated_next_position = after_next_position.translate_to_matrix_position(self.level.matrix)
        next_pos_char = self.level.matrix[translated_position.y][translated_position.x]
        after_next_pos_char = self.level.matrix[translated_next_position.y][translated_next_position.x]

        if next_pos_char == LevelBlock.EMPTY_BLOCK or next_pos_char == LevelBlock.GOAL_BLOCK:
            self.end_move_execute(next_position, move_character_minor)
        elif next_pos_char == LevelBlock.BOX_BLOCK  and after_next_pos_char == LevelBlock.EMPTY_BLOCK:
            self.update_level_on_block_push(translated_position, translated_next_position, LevelBlock.EMPTY_BLOCK,  LevelBlock.BOX_BLOCK)
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == LevelBlock.BOX_BLOCK and after_next_pos_char == LevelBlock.GOAL_BLOCK:
            self.update_level_on_block_push(translated_position, translated_next_position, LevelBlock.EMPTY_BLOCK, LevelBlock.BOX_UNDER_GOAL_BLOCK)
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == LevelBlock.BOX_UNDER_GOAL_BLOCK and after_next_pos_char == LevelBlock.GOAL_BLOCK:
            self.update_level_on_block_push(translated_position, translated_next_position, LevelBlock.GOAL_BLOCK, LevelBlock.BOX_UNDER_GOAL_BLOCK)
            self.end_move_execute(next_position, move_character_major)
        elif next_pos_char == LevelBlock.BOX_UNDER_GOAL_BLOCK and after_next_pos_char == LevelBlock.EMPTY_BLOCK:
            self.update_level_on_block_push(translated_position, translated_next_position, LevelBlock.GOAL_BLOCK,  LevelBlock.BOX_BLOCK)
            self.end_move_execute(next_position, move_character_major)

    def end_move_execute(self, next_position, move_character):
        self.set_player_params('n_moves', 1)
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

    def set_player_params(self, param, modifier):
        self.player_params[param] += (not self.is_animation) * modifier

    def set_animation(self, is_animation):
        self.is_animation = is_animation

    def print_movements(self):
        print(self.player_movements)

    def print_player_params(self):
        print(self.player_params)