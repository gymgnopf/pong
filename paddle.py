import pygame
from constants import *
from rectangle import Rectangle

class Paddle(Rectangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


    def update(self, dt, game_state):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move_up(dt * -1)
        if (keys[pygame.K_s]):
            self.move_down(dt)

    def move_up(self, dt):
        self.obj.y += int(PADDLE_SPEED * dt)
        self.obj.y = max([0, self.obj.y])

    def move_down(self, dt):
        self.obj.y += int(PADDLE_SPEED * dt)
        # Wenn Y-Position von Paddle grösser als die Y-Achse minus die Paddlehöhe ist,
        # dann nehme die VIRTUAL_HEIGHT - PADDLE_HEIGHT als neue Position.
        # So wird verhindert, dass das Paddle sich aus dem Fenster bewegt.
        self.obj.y = min([VIRTUAL_HEIGHT - PADDLE_HEIGHT, self.obj.y])