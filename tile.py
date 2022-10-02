import time
import pygame
import globals as g


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.image = pygame.Surface((g.CELLSIZE, g.CELLSIZE))
        self.image = g.bg_images[tile_type]
        self.rect = pygame.Rect(x, y, g.CELLSIZE, g.CELLSIZE)
        self.tile_type = tile_type

    def update(self):
        pass

    def draw(self, camera):
        g.DISPLAYSURF.blit(self.image, ((self.rect.x + camera.X_OFFSET) *
                                        g.CELLSIZE, (self.rect.y + camera.Y_OFFSET) * g.CELLSIZE))
