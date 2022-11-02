from pico2d import *

#이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, A= range(6)

#키 입력확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD, 
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): A
}

#IDLE 클래스는 변수와 함수를 IDLE라는 이름으로 모아주려고 하는것이다. (객체 만드려는게 아님)
class IDLE:
    def enter(self, event): #상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000
        pass
    def exit(self): #상태를 나올때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        pass
    def do(self): #상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)




class RUN:
    @staticmethod #데코레이터이다. 클래수 함수라는 걸 알리는 거다. 안써도 큰상관 없음
    def enter(self, event): #IDLE에서 run으로 들어올때 어떤 키를 눌렀기 때문에 run에 들어왔는지 판단
        print('ENTER RUN')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        #키 이벤트 정보가 필요하다.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event): #상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        pass
    def exit(self): #상태를 나올때 행하는 액션
        print('EXIT IDLE')
        pass
    def do(self): #상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '',
                                           self.x -25, self.y-25, 100, 100)
        else: #오른쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2, '',
                                           self.x -25, self.y-25, 100, 100)

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        if self.dir == 1:
            self.x += 1
        elif self.dir == -1:
            self.x -= 1
        else:
            self.dir = 1

    @staticmethod
    def exit(self):
        self.face_dir = self.dir  # 달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        if self.x >= 780:
            self.dir = -1
        elif self.x <= 20:
            self.dir = 1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+45, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+45, 200, 200)


#상태변환 기술
next_state = {
    AUTO_RUN: {RD: RUN, LD: RUN, A: IDLE, RU: RUN, LU: RUN},
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP, A: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, A: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD:IDLE, LD: IDLE, A: AUTO_RUN }
}




class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self) #현재 상태의 do액션 수행

        #이벤트를 확인해서 , 이벤트가 발생했으면,
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self) #현재 상태를 나가야 되고.
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 구한다.
            self.cur_state.enter(self, event) #다음 상태의 entry action 수행


        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        

    def draw(self):
        self.cur_state.draw(self)