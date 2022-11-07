from pico2d import *

class Grass:
    def __init__(self, x, y):
        self.image = load_image('grass.png')
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


