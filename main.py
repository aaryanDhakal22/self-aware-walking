import pygame
from board import Board
from pygame.locals import K_ESCAPE,KEYDOWN
from pprint import pprint
from bot import Bot

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

running  = True
new_board = Board()
new_board.fill_dots()
print(new_board.nodes)


player = Bot(new_board)
player.move_up()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

    screen.blit(new_board.surf,(100,100))
    pygame.display.flip()


pygame.quit()