from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
   global running
   global x
   global dir_x
   global dir_y

   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type==SDL_KEYDOWN:
           if event.key == SDLK_RIGHT:
               dir_x += 1
           elif event.key == SDLK_LEFT:
               dir_x -= 1
           elif event.key == SDLK_UP:
               dir_y += 1
           elif event.key == SDLK_DOWN:
               dir_y -= 1

           elif event.key == SDLK_ESCAPE:
               running =False
       elif event.type == SDL_KEYUP:
           if event.key == SDLK_RIGHT:
               dir_x -= 1
           elif event.key == SDLK_LEFT:
               dir_x += 1
           elif event.key == SDLK_UP:
               dir_y -= 1
           elif event.key == SDLK_DOWN:
               dir_y += 1


open_canvas()
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
a=0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y * 5


    if dir_x == 0:
        if a==1:
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        elif a==0:
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
    if dir_x < 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        a=0
    elif dir_x > 0 :
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        a=1

    update_canvas()

    if (x>770):
        x -= dir_x * 5
    elif(x<30):
        x -= dir_x *5
    elif(y<25):
        y -= dir_y *5
    elif(y>575):
        y -= dir_y *5

    delay(0.01)

close_canvas()

