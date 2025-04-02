import pygame

class Paddle:

    def __init__(self, x):
        self.x = x
        self.y = 0
        self.width = 20
        self.height = 80
        self.dy = 0

    def move(self, y, w_height):
        self.y += y
        self.y = max(0, min(self.y, w_height - self.height))

    def render(self, display, color):
        paddle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display, color, paddle)