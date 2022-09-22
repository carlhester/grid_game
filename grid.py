import pygame
import sys
import random
from player import *
from pygame.locals import *
import globals as g


# assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
# assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"


def main():
    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    g.DISPLAYSURF = pygame.display.set_mode((g.SCREENWIDTH, g.SCREENHEIGHT))

    basicfont = pygame.font.SysFont(None, 32, 0, 1)

    bg_images = generate_map_images()
    g.NEXTMOVE = 0

    player = Player(5, 4)
    badguy = BadGuy(5, 5, "shyguy")

    mapX = 0
    mapY = 0
    wallGroup = []
    bgGroup = []
    connGroup = []
    shotGroup = []
    coinGroup = []
    keyGroup = []
    doorGroup = []
    message = Message()
    create_level(levels[mapX][mapY], bgGroup, wallGroup,
                 player, connGroup, coinGroup, keyGroup, doorGroup)

    GAMERUNNING = True
    while GAMERUNNING == True:
        pygame.display.set_caption(
            str(player.x) + ":" + str(player.y) + "\t" + str(mapX) + ":" + str(mapY))
        draw_level(bgGroup, bg_images, coinGroup, keyGroup, doorGroup)
        getInput(player, message, shotGroup)
        player.update(wallGroup, connGroup, bgGroup, message,
                      coinGroup, keyGroup, doorGroup)
        badguy.update(wallGroup)
        g.NEXTMOVE = 0
        badguy.draw()
        player.draw()
        drawGrid()
        for shot in shotGroup:
            shot.update(shotGroup)
            shot.draw()
        drawHearts(player)
        message.draw(basicfont)
        pygame.display.update()
        FPSCLOCK.tick(g.FPS)


def brickClearScreen():
    # this doesn't work on OSX :(
    global DISPLAYSURF
    width = 30
    height = 10
    DISPLAYSURF.fill((255, 255, 255))
    pygame.display.update()
    for x in range(0, g.SCREENWIDTH, width):
        for y in range(0, g.SCREENHEIGHT, height):
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (x, y, width, height))
            pygame.display.update()


class Shot():
    def __init__(self, player):
        self.shot_img = pygame.image.load('images/shot.png')
        self.shot_img = pygame.transform.scale(
            self.shot_img, (g.CELLSIZE, g.CELLSIZE))
        self.shot_img_up = pygame.transform.rotate(self.shot_img, -90)
        self.shot_img_down = pygame.transform.rotate(self.shot_img, 90)
        self.shot_img_right = pygame.transform.flip(self.shot_img, 1, 0)
        self.facing = player.facing
        self.speed = 30
        self.x = player.x * g.CELLSIZE
        self.y = player.y * g.CELLSIZE

    def update(self, shotGroup):
        if self.y > g.SCREENHEIGHT or self.y < 0 or self.x > g.SCREENWIDTH or self.x < 0:
            shotGroup.remove(self)

        if self.facing == 1 and self.y <= g.SCREENHEIGHT:
            self.y += self.speed
        elif self.facing == 3 and self.y >= -5:
            self.y -= self.speed
        elif self.facing == 0 and self.x <= g.SCREENWIDTH:
            self.x += self.speed
        elif self.facing == 2 and self.x > -5:
            self.x -= self.speed

    def draw(self):
        if self.facing == 1:
            self.shot_img = self.shot_img_down
        if self.facing == 0:
            self.shot_img = self.shot_img_right
        if self.facing == 3:
            self.shot_img = self.shot_img_up
        DISPLAYSURF.blit(self.shot_img, (self.x, self.y))


class Boss():
    def __init__(self):
        pass

    def update():
        pass

    def draw():
        pass


class Message():
    def __init__(self):
        self.text = ""

    def update(self, text):
        self.text = text

    def draw(self, basicfont):
        if self.text != "":
            width = int(g.SCREENWIDTH * .8)
            height = int(g.SCREENHEIGHT / 5)
            left = int(g.SCREENWIDTH - width) / 2
            top = int((g.SCREENHEIGHT / 5))
            textlength = len(self.text)
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0),
                             (left, top, width, height))
            text = basicfont.render(
                self.text, False, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = left + (((width) / 2) - (textlength/2))
            textrect.y = top + (height / 2)
            DISPLAYSURF.blit(text, textrect)

    def clear(self):
        self.text = ""


def drawHearts(player):
    heart_img = pygame.image.load('images/heart.png')
    heart_img = pygame.transform.scale(heart_img, (20, 20))
    spacing = 10
    if player.hitpoints > 0:
        for heart in range(1, player.hitpoints + 1):
            g.DISPLAYSURF.blit(heart_img, (spacing, 10))
            spacing += 30


def drawGrid():
    for x in range(0, g.SCREENWIDTH, g.CELLSIZE):
        pygame.draw.line(g.DISPLAYSURF, (100, 100, 100),
                         (x, 0), (x, g.SCREENHEIGHT))
    for y in range(0, g.SCREENHEIGHT, g.CELLSIZE):
        pygame.draw.line(g.DISPLAYSURF, (100, 100, 100),
                         (0, y), (g.SCREENWIDTH, y))


def getInput(player, message, shotGroup):

    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            message.clear()
            if len(shotGroup) < 3:
                shot = Shot(player)
                shotGroup.append(shot)
        if event.type == pygame.KEYUP and event.key == pygame.K_z:
            message.update("This is a dangerous place!")
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.moving_down = 1
            player.facing = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.moving_up = 1
            player.facing = 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.moving_right = 1
            player.facing = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.moving_left = 1
            player.facing = 2

        if event.type == pygame.KEYUP and event.key == pygame.K_o:
            if player.hitpoints > 0:
                player.hitpoints -= 1

        if event.type == pygame.KEYUP and event.key == pygame.K_p:
            player.hitpoints += 1

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player.moving_down = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player.moving_up = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            player.moving_right = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            player.moving_left = 0


class BadGuy():
    def __init__(self, x, y, badguytype):
        self.badguy_img = pygame.image.load('images/badguy.png')
        self.badguy_img = pygame.transform.scale(
            self.badguy_img, (g.CELLSIZE, g.CELLSIZE))
        self.x = x
        self.y = y
        self.badguytype = badguytype
        self.moving_direction = 0
        self.distance_traveled = 0

    def update(self, wallGroup):
        if g.NEXTMOVE == 1:
            current_x = self.x
            current_y = self.y
            if self.distance_traveled < 3:
                if self.moving_direction == 0:
                    self.x += 1
                if self.moving_direction == 1:
                    self.y += 1
                if self.moving_direction == 2:
                    self.x -= 1
                if self.moving_direction == 3:
                    self.y -= 1
                self.distance_traveled += 1
            else:
                self.distance_traveled = 0
                self.moving_direction = random.randint(0, 4)
            if (self.x, self.y) in wallGroup:
                self.x = current_x
                self.y = current_y

    def draw(self):
        g.DISPLAYSURF.blit(self.badguy_img, (self.x *
                                             g.CELLSIZE, self.y * g.CELLSIZE))


def generate_map_images():
    key_img = pygame.image.load('images/key.png')
    key_img = pygame.transform.scale(key_img, ((g.CELLSIZE, g.CELLSIZE)))
    coin_img = pygame.image.load('images/coin.png')
    coin_img = pygame.transform.scale(coin_img, ((g.CELLSIZE, g.CELLSIZE)))
    door_img = pygame.image.load('images/door.png')
    door_img = pygame.transform.scale(door_img, ((g.CELLSIZE, g.CELLSIZE)))
    grass_img = pygame.image.load('images/grass.png')
    grass_img = pygame.transform.scale(grass_img, ((g.CELLSIZE, g.CELLSIZE)))
    wall_img = pygame.image.load('images/wall.png')
    wall_img = pygame.transform.scale(wall_img, ((g.CELLSIZE, g.CELLSIZE)))
    sand_img = pygame.image.load('images/sand.png')
    sand_img = pygame.transform.scale(sand_img, ((g.CELLSIZE, g.CELLSIZE)))

    rock_spritesheet = pygame.image.load('images/rock_spritesheet.png')
    rock_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
    rock_surf.blit(rock_spritesheet, (-70, 0))
    rock1_img = pygame.transform.scale(rock_surf, (g.CELLSIZE, g.CELLSIZE))
    rock_surf.blit(rock_spritesheet, (-35, 0))
    rock2_img = pygame.transform.scale(rock_surf, (g.CELLSIZE, g.CELLSIZE))
    rock_surf.blit(rock_spritesheet, (0, 0))
    rock3_img = pygame.transform.scale(rock_surf, (g.CELLSIZE, g.CELLSIZE))

    bg_images = {}
    bg_images = {'key': key_img, 'coin': coin_img, 'door': door_img, 'grass': grass_img,
                 'wall': wall_img, 'rock1': rock1_img, 'rock2': rock2_img, 'rock3': rock3_img, 'sand': sand_img}
    return bg_images


if __name__ == '__main__':
    main()
