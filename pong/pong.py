import pygame
import sys

from paddle import Paddle
from ball import Ball

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (40, 45, 52)

FPS = 60

PADDLE_SPEED = 15
BALL_SPEED = 5

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

font = pygame.font.Font('font.ttf', 48)

player1_y = 30
player2_y = WINDOW_HEIGHT - 120

# player 1
player1 = Paddle(30)

# player 2
player2 = Paddle(WINDOW_WIDTH - 50)

# Ball
ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, BALL_SPEED)

running = True
while running:
    display.fill(GREY)

    text = font.render('Welcome to Pong!', True, WHITE)
    display.blit(text, (WINDOW_WIDTH / 2 - 190, WINDOW_HEIGHT / 2 - 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move(-PADDLE_SPEED, WINDOW_HEIGHT)
        
    if keys[pygame.K_s]:
        player1.move(PADDLE_SPEED, WINDOW_HEIGHT)
        
    if keys[pygame.K_UP]:
        player2.move(-PADDLE_SPEED, WINDOW_HEIGHT)

    if keys[pygame.K_DOWN]:
        player2.move(PADDLE_SPEED, WINDOW_HEIGHT)

    # Ball
    ball.move(WINDOW_HEIGHT)

    # if ball.x <= 0 or ball.x >= WINDOW_WIDTH:
    #     ball.reset()

    player1.render(display, WHITE)
    player2.render(display, WHITE)
    ball.render(display, WHITE)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()