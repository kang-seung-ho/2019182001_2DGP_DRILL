import pico2d
import game_framework
import play_state
import item_state
import logo_state
pico2d.open_canvas()
# game_framework.run(logo_state)
game_framework.run(play_state) #테스트를 위해 로고말고 바로 들어감
pico2d.clear_canvas()

