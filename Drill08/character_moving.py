from pico2d import *
T_WIDTH, T_HEIGHT = 1280, 1024



def handle_events():
    global running
    global dirx
    global diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1


def character_draw(loaction, x,y):
    character.clip_draw(frame*100,100*loaction,100,100,x, y)

open_canvas(T_WIDTH,T_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
frame = 0

dirx, diry = 0,0
x = T_WIDTH//2
y = T_HEIGHT//2


while running:
    clear_canvas()
    background.draw(T_WIDTH//2, T_HEIGHT//2)
    leftright = 0

    if x+dirx*5 == x and y+diry*5 == y:
        if  leftright == 2:
            character_draw(2, x, y)
        elif leftright == 3:
            character_draw(3, x, y)
        elif leftright == 0:
            character_draw(3, x, y)
    elif x+dirx*5>=1280:
        character_draw(3,1280,y)
    elif x+dirx*5<=0:
        character_draw(2,0,y)
    elif y+diry*5>=1024:
        if leftright == 1:
            character_draw(2,x,1024)
    elif y+diry*5>=1024:
        if leftright == 2:
            character_draw(3,x,1024)
    elif y+diry*5<=0:
        character_draw(2,x,0)
    elif x+dirx * 5>x:
        character_draw(1,x,y)
        leftright = 1
    elif x+ dirx * 5 < x:
        character_draw(0,x,y)
        leftright = 2
    elif x+dirx*5 == x and leftright == 2:
        character_draw(2,x,y)
    elif x+dirx*5 == x and leftright == 1:
        character_draw(3,x,y)
    elif y+diry*5>y:
        character_draw(1,x,y)
    elif y+diry*5< y:
        character_draw(0,x,y)

    update_canvas()
    handle_events()
    frame = (frame + 1)%8
    x += dirx * 5
    y += diry * 5
    delay(0.01)

close_canvas()