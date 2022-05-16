import pygame


class Path(pygame.sprite.Sprite):
    def __init__(self, cords1, cords2):
        super(Path, self).__init__()
        self.surf = pygame.Surface()
