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