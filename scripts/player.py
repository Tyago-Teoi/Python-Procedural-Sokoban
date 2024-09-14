import arcade

class Player:
    level = None
    level_matrix = None
    SPRITE_SIZE = 0
    SPRITE_ADJUSTMENT_X = 30
    SPRITE_ADJUSTMENT_Y = 40
    x = 0
    y = 0
    sprite = None

    asdf= 0
    asd = 0

    def __init__(self, level, sprite_size):
        self.level = level
        self.level_matrix = level.matrix
        self.SPRITE_SIZE = sprite_size
        self.set_player_initial_position()
        self.set_player_sprite()

    def set_player_initial_position(self):
        for i in range(len(self.level.matrix)):
            for j in range(len(self.level.matrix[0])):
                if self.level.matrix[i][j] == '@':
                    print('i = {a}'.format(a=i))
                    print('j = {a}'.format(a=j))
                    self.x = j
                    self.y = len(self.level.matrix) - i - 1
                    return True
        return False

    def set_player_sprite(self):
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5
        )
        self.update_player_position()

    def move_up(self):
        #self.asdf += 1
        #self.asd += 1
        #self.level.matrix[self.asd][self.asdf] = '-'
        if self.level.matrix[len(self.level.matrix) - self.y - 1 - 1][self.x] != '#':
            self.y += 1
            self.update_player_position()

        #self.level.update_level()

    def move_down(self):
        if self.level.matrix[len(self.level.matrix) - self.y - 1 + 1][self.x] != '#':
            self.y -= 1
            self.update_player_position()

    def move_left(self):
        if self.level.matrix[len(self.level.matrix) - self.y - 1][self.x - 1] != '#':
            self.x -= 1
            self.update_player_position()

    def move_right(self):
        if self.level.matrix[len(self.level.matrix) - self.y - 1][self.x + 1] != '#':
            self.x += 1
            self.update_player_position()

    def update_player_position(self):
        self.sprite.center_x = self.x * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_X
        self.sprite.center_y = self.y * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_Y