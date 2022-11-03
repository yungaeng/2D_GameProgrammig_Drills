from pico2d import *
import game_world


# 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AD, SPACE = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


# 함수를 그룹으로 묶으려고 클래스를 이용
# 스테이트를 구현 -클래스를 이용해서-
class IDLE:

    def enter(self, event):
        print('ENTER IDLE')
        self.timer = 1000
        self.dir = 0

    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.fire_ball()

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:

    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir
        if event == SPACE:
            self.fire_ball()

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        print('EXIT SLEEP')
        if event == SPACE:
            self.fire_ball()

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        print('DRAW SLEEP')
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '',
                                           self.x - 25, self.y - 25, 100, 100)


class AUTO_RUN:

    def enter(self, event):
        print('ENTER AUTO_RUN')


    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x == 0:
            self.dir += 1
        elif self.x == 800:
            self.dir -= 1
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 200, 200)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN, SPACE: IDLE},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, AD: AUTO_RUN, SPACE: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: SLEEP, SPACE: SLEEP},
    AUTO_RUN: {AD: IDLE, RU: RUN, LU: RUN, RD: RUN, LD: RUN}
}


class Boy:

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_que = []

        # 초기 상태 설정과 엔트리
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        # 이벤트가 들어있으면 현재상태를 나가고
        # 다음 상태를 계산하여 다음상태에 들어간다

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(self.cur_state, event)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE BALL')
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)