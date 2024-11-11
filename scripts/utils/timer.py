import arcade

class Timer:
    time = 0
    def __init__(self):
        self.time = 0

    def update(self, delta_time):
        self.time += delta_time

    def reset(self):
        self.time = 0

    def print(self):
        print('{a} minutes and {b} seconds'.format(a = int(self.time/60), b = int(self.time%60)))