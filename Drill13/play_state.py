from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy


boy = None
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = Boy()
    boy2 = Boy()
    boy3 = Boy()
    boy4 = Boy()
    boy5 = Boy()
    boy6 = Boy()
    boy7 = Boy()
    boy8 = Boy()
    boy9 = Boy()
    boy10 = Boy()

    grass = Grass()
    game_world.add_object(grass, 0)

    game_world.add_object(boy, 1)
    game_world.add_object(boy2, 1)
    game_world.add_object(boy3, 1)
    game_world.add_object(boy4, 1)
    game_world.add_object(boy5, 1)
    game_world.add_object(boy6, 1)
    game_world.add_object(boy7, 1)
    game_world.add_object(boy8, 1)
    game_world.add_object(boy9, 1)
    game_world.add_object(boy10, 1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas(1600, 600)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
