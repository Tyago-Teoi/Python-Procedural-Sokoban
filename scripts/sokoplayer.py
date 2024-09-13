import arcade

class Player:
    SPRITE_SIZE = 0
    SPRITE_ADJUSTMENT_X = 30
    SPRITE_ADJUSTMENT_Y = 40
    x = 0
    y = 0
    sprite = None

    def __init__(self, level, sprite_size):
        self.SPRITE_SIZE = sprite_size
        self.set_player_initial_position(level)
        self.set_player_sprite()

    def set_player_initial_position(self, level):
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
        self.sprite.center_x = self.x * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_X
        self.sprite.center_y = self.y * self.SPRITE_SIZE + self.SPRITE_ADJUSTMENT_Y

