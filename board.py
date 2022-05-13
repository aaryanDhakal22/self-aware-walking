import pygame
from node import Node
from pprint import pprint


class Board(pygame.sprite.Sprite):
    def __init__(self):
        super(Board, self).__init__()
        self.surf = pygame.Surface((400, 400))
        self.surf.fill((50, 50, 50))
        self.rect = self.surf.get_rect()
        self.nodes = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def fill_dots(self):
        for i in range(1, 11):
            for j in range(1, 11):
                x_loc = j * 40
                y_loc = i * 40
                new_Node = Node(x=x_loc, y=y_loc,ar_y=(i-1),ar_x=(j-1))
                self.surf.blit(new_Node.surf, (x_loc, y_loc))
                self.nodes[i-1][j-1] = new_Node
                # print(self.nodes)
                # print("("+str(x_loc)+","+str(y_loc)+")")
                # print("("+str(i-1)+","+str(j-1)+")")
