import pygame
from stackType import Stack
from random import randint as rd
from time import sleep 

class Bot(pygame.sprite.Sprite):
    def __init__(self, board):
        super(Bot, self).__init__()
        self.board = board
        self.node_list = board.nodes
        self.travelled_node = Stack()
        self.loc = board.nodes[0][0]
        self.loc.visited = True
        self.travelled_node.queue(self.loc)
        self.color = 1

    def connect_node(self, to_node):

        if not to_node.visited:
            print("Not Visited Nod")
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
            return "CONNECT"
        else:
            print("Visited Node")
            return "VISITED"

    def move_up(self):
        if self.loc.ar_y != 0:
            to_node = self.node_list[self.loc.ar_y - 1][self.loc.ar_x]
            status = self.connect_node(to_node)

            return status
        else:
            print("BOUNDRY")

    def move_down(self):
        if self.loc.ar_y != 9:
            to_node = self.node_list[self.loc.ar_y + 1][self.loc.ar_x]
            status = self.connect_node(to_node)

            return status
        else:
            print("BOUNDRY")

    def move_left(self):
        if self.loc.ar_x != 0:
            to_node = self.node_list[self.loc.ar_y][self.loc.ar_x - 1]
            status = self.connect_node(to_node)

            return status
        else:
            print("BOUNDRY")

    def move_right(self):
        if self.loc.ar_x != 9:
            to_node = self.node_list[self.loc.ar_y][self.loc.ar_x + 1]
            status = self.connect_node(to_node)
            return status
        else:
            print("BOUNDRY")

    def gen_maze(self):
        prev_choice = []
        restrict = ""
        strike = 0
        while self.travelled_node.size != 20:
            choice = rd(0, 3)
            while True:
                print("choice",choice)
                print("prev", prev_choice)
                if choice == 0 and restrict != 0:
                    status = self.move_up()
                    if status == "CONNECT":
                        prev_choice.append(0)
                        break
                    else:
                        choice += 1
                        strike += 1

                if choice == 1 and restrict != 1:
                    status = self.move_down()
                    if status == "CONNECT":
                        prev_choice.append(1)
                        break
                    else:
                        choice += 1
                        strike += 1

                if choice == 2 and restrict != 2:
                    status = self.move_left()
                    if status == "CONNECT":
                        prev_choice.append(2)
                        break
                    else:
                        choice += 1
                        strike += 1

                if choice == 3 and restrict != 3:
                    status = self.move_right()
                    if status == "CONNECT":
                        prev_choice.append(3)
                        break
                    else:
                        choice += 1
                        strike += 1
                if choice >= 4 and strike >= 4:
                    print("MISTAKE WAS MADE SO GO THE FUCK BACK BRUHHHHH")
                    self.loc.visited = False
                    self.loc = self.travelled_node.dequeue()
                    restrict = prev_choice.pop(-1)
                    c
                    sleep(4)
                else:
                    choice = 0
                    strike = 0
                    sleep(1)
            restrict = ""
            strike = 0
