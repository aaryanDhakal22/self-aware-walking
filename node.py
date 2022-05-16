import pygame


class Node(pygame.sprite.Sprite):
    def __init__(self, x, y, ar_x, ar_y):
        super(Node, self).__init__()
        self.x = x
        self.y = y
        self.ar_x = ar_x
        self.ar_y = ar_y
        self.visited = False
        self.cords = (self.x + 5, self.y + 5)
        self.node_radius = 10
        self.center = (5, 5)
        self.surf = pygame.Surface((self.node_radius, self.node_radius))
        self.surf.fill((50, 50, 50))
        pygame.draw.circle(self.surf, (255, 255, 255), self.center, 5)
        self.rect = self.surf.get_rect()

    def __repr__(self):
        return "Node < " + str(self.x) + " " + str(self.y) + " >"
