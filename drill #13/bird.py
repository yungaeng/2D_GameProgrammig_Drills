from pico2d import *
import game_framework

Brid_Vac = 1.0
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 1

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x = self.x + Brid_Vac * game_framework.frame_time
        if self.x == 1600:
            self.dir = -1
        elif self.x == 0:
            self. dir = 1

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 183, 336, 183, 183, self.x, self.y)
        else:
            self.image.clip_camposite_draw(int(self.frame) * 183, 336, 183, 183, 3.141592 / 2, '', self.x, self.y)


class Bird:

    def __init__(self):
        self.x, self.y = 100, 300
        self.frame = 0
        self.dir = 0
        self.image = load_image('bird_animation.png')
        self.cur_state = IDLE

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

