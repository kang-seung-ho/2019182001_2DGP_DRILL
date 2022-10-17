from pico2d import *
import game_framework
import logo_state
import title_state
import item_state
import random

boy_num = 1

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')


    def update(self):
        self.frame = random.randint(0, 7)
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1



    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)


# open_canvas()

boy = None
grass = None


team = []

# running = True
#초기화
def enter():
    global boy, grass, running
    global team
    team.append(Boy()) #객체 생성
    grass = Grass()
    running = True

#종료
def exit():
    global boy, grass, team
    del boy
    del grass

#월드에 존재하는 객체들을 업데이트
def update():
    for boy in team:
        boy.update()
    # grass는 update 필요없음

#world를 그린다.
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in team:
        boy.draw()


def pause():
    pass

def resume():
    pass

# running = True
# while running:
#     handle_events()
#     for boy in team():
#         boy.update()
#     clear_canvas()
#     draw_world()
#     update_canvas()
#
#     delay(0.05)