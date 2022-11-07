from pico2d import *
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.timer -= 1

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 183, 336, 183, 183, self.x, self.y)
        else:
            self.image.clip_camposite_draw(int(self.frame) * 183, 336, 183, 183, , , self.x, self.y)


class Bird:

    def __init__(self):
        self.x, self.y = 100, 70
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        pass

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)
