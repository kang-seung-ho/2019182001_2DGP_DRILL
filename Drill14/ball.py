import random
from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        Ball.image = load_image('ball21x21.png')
        self.x, self.y,  = random.randint(0, 1600), random.randint(10, 1000)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h




    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        # self.image.clip_draw_to_origin(
        #     self.window_left, self.window_bottom,
        #     20, 20,
        #     self.x, self.y
        # )

        # draw_rectangle(*self.get_bb())

    def update(self):
        self.window_left = clamp(0,
                                 int(server.boy.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.boy.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
            game_world.ball_cnt += 1