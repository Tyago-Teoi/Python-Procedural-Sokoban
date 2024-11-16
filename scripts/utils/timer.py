import arcade

class Timer():
    total_time = 0
    level_time : float = 0
    def __init__(self):
        self.total_time = 0
        self.level_time = 0

    def on_update(self, delta_time):
        self.total_time += delta_time
        self.level_time += delta_time

    def reset(self):
        self.level_time = 0

    def reset_all(self):
        self.total_time = 0
        self.level_time = 0

    def print(self):
        print('{a} minutes and {b} seconds'.format(a = int(self.time/60), b = int(self.time%60)))