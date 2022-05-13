import pygame
from stackType import Stack
from board import Board
from path import Path
class Bot(pygame.sprite.Sprite):

    def __init__(self,board):
        super(Bot,self).__init__()
        self.board = board
        self.node_list = board.nodes
        self.travelled_node = Stack()
        self.loc = board.nodes[4][4]
        self.travelled_node.queue(self.loc)

    def connect_node(self,to_node):
        self.travelled_node.queue(to_node)
        pygame.draw.line(self.board.surf,(255,255,255),self.loc.cords,to_node.cords,5)
        self.loc = self.travelled_node.last_item()

    def move_up(self):
        if self.loc.ar_x == 0:
            return False
        else:
            to_node =  self.node_list[self.loc.ar_y - 1][self.loc.ar_x]
            self.connect_node(to_node)
