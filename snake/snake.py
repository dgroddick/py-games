import pygame
import random
import sys

pygame.init()

# define basic colours
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# the snake
snake_block = 10
snake_speed = 15

game_font = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 35)

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, WHITE, [x[0], x[1], snake_block, snake_block])

def message(msg, colour):
    mesg = game_font.render(msg, True, colour)
    display.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT  /3])

def game_loop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(BLUE)
            message("You Lost! Press 'Q' to Quit or 'C' to play again", RED)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(BLACK)
        pygame.draw.rect(display, GREEN, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            print("yum yum")

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()
    pygame.quit()
    sys.exit()
