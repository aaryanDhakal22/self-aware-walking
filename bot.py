import pygame
from stackType import Stack
from board import Board
from path import Path


class Bot(pygame.sprite.Sprite):
    def __init__(self, board):
        super(Bot, self).__init__()
        self.board = board
        self.node_list = board.nodes
        self.travelled_node = Stack()
        self.loc = board.nodes[2][4]
        self.loc.visited = True
        self.travelled_node.queue(self.loc)
        self.color = 1

    def connect_node(self, to_node):
        if not to_node.visited:
            print("Not Visited Nod\n")
            self.travelled_node.queue(to_node)

            if self.color % 3 == 0:
                use = (255, 0, 0)
            if self.color % 3 == 1:
                use = (0, 255, 0)
            if self.color % 3 == 2:
                use = (0, 0, 255)
            pygame.draw.line(self.board.surf, use, self.loc.cords, to_node.cords, 5)
            self.loc = self.travelled_node.last_item()
            to_node.visited = True
            self.color += 1
        else:
            print("Visited Node\n")
            return False

    def move_up(self):
        if self.loc.ar_y != 0:
            to_node = self.node_list[self.loc.ar_y - 1][self.loc.ar_x]
            self.connect_node(to_node)
        else:
            print("Boundry Hit")
            print(self.loc.ar_y, self.loc.ar_x)

    def move_down(self):
        if self.loc.ar_y != 9:
            to_node = self.node_list[self.loc.ar_y + 1][self.loc.ar_x]
            self.connect_node(to_node)
        else:
            print("Boundry Hit")

    def move_left(self):
        if self.loc.ar_x != 0:
            to_node = self.node_list[self.loc.ar_y][self.loc.ar_x - 1]
            self.connect_node(to_node)
        else:
            print("Boundry Hit")

    def move_right(self):
        if self.loc.ar_x != 9:
            to_node = self.node_list[self.loc.ar_y][self.loc.ar_x + 1]
            self.connect_node(to_node)
        else:
            print("Boundry Hit")
