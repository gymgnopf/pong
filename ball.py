import pygame
import random
from constants import *
from rectangle import Rectangle
from debug import Debug

class Ball(Rectangle):


    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 100 if random.randint(0, 1) == 1 else -100
        self.dy = random.randint(-50, 50)

    def reset(self):
        self.obj.x = VIRTUAL_WIDTH / 2 - 2
        self.obj.y = VIRTUAL_HEIGHT / 2 - 2
        self.dx = 100 if random.randint(0, 1) == 1 else -100
        self.dy = random.randint(-50, 50)

    def update(self, dt, game_state):
        if game_state == "play":

            if self.obj.y <= 0:
                self.obj.y = 0
                self.dy = -self.dy
            
            if self.obj.y >= VIRTUAL_HEIGHT - 4:
                self.obj.y = VIRTUAL_HEIGHT - 4
                self.dy = -1 * self.dy
            

            self.obj.x += self.dx * dt
            self.obj.y += self.dy * dt
    
    def bounceOff(self, paddle):
        self.dx = -1 * self.dx * 1.03
        self.x = paddle.obj.x + 5
        
        if self.dy < 0:
            self.dy = -1 * random.randint(10, 150)
        else:
            self.dy = random.randint(10, 150)