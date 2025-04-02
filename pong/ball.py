import pygame
import random

class Ball:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = speed
        self.dx = random.choice([-self.speed, self.speed])
        self.dy = random.choice([-self.speed, self.speed])

    def move(self, w_height):
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0 or self.y >= w_height:
            self.dy *= -1

    def render(self, display, color):
        ball = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display, color, ball)

    def reset(self):
        self.__init__()