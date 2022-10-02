import pygame


def generate_map_images():
    key_img = pygame.image.load('images/key.png')
    key_img = pygame.transform.scale(key_img, ((CELLSIZE, CELLSIZE)))
    coin_img = pygame.image.load('images/coin.png')
    coin_img = pygame.transform.scale(coin_img, ((CELLSIZE, CELLSIZE)))
    door_img = pygame.image.load('images/door.png')
    door_img = pygame.transform.scale(door_img, ((CELLSIZE, CELLSIZE)))
    grass_img = pygame.image.load('images/grass.png')
    grass_img = pygame.transform.scale(grass_img, ((CELLSIZE, CELLSIZE)))
    wall_img = pygame.image.load('images/wall.png')
    wall_img = pygame.transform.scale(wall_img, ((CELLSIZE, CELLSIZE)))
    sand_img = pygame.image.load('images/sand.png')
    sand_img = pygame.transform.scale(sand_img, ((CELLSIZE, CELLSIZE)))

    rock_spritesheet = pygame.image.load('images/rock_spritesheet.png')
    rock_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
    rock_surf.blit(rock_spritesheet, (-70, 0))
    rock1_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))
    rock_surf.blit(rock_spritesheet, (-35, 0))
    rock2_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))
    rock_surf.blit(rock_spritesheet, (0, 0))
    rock3_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))

    images = {}
    images = {'k': key_img,
              'C': coin_img,
              'D': door_img,
              'g': grass_img,
              '.': grass_img,
              'X': grass_img,
              '#': wall_img,
              'o': rock1_img,
              'O': rock2_img,
              '0': rock3_img,
              '*': sand_img}
    return images


# DISPLAYSURF = None
FPS = 30
CELLSIZE = 50
STEPSIZE = (CELLSIZE/2)
SCREENWIDTH = 600
SCREENHEIGHT = 600
BLACK = (0, 0, 0)
bg_images = generate_map_images()
