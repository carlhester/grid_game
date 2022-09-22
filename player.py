
import pygame
import levels
from levels import *
import globals as g


class Player():
    def __init__(self, x, y):
        # global CELLSIZE, SCREENWIDTH, SCREENHEIGHT, DISPLAYSURF
        self.spritesheet = pygame.image.load('images/hero_spritesheet.png')

        self.player_img_list = []
        self.player_img_back_list = []
        self.player_img_right_list = []
        self.player_img_left_list = []

        # walking down
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, 0))
        self.player_img = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_list.append(self.player_img)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, 0))
        self.player_img = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_list.append(self.player_img)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, 0))
        self.player_img = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_list.append(self.player_img)

        # walking up
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -96))
        self.player_img_back = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -96))
        self.player_img_back = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -96))
        self.player_img_back = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)

        # walking right
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -64))
        self.player_img_right = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -64))
        self.player_img_right = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -64))
        self.player_img_right = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)

        # walking left
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -32))
        self.player_img_left = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -32))
        self.player_img_left = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -32))
        self.player_img_left = pygame.transform.scale(
            self.player_surf, (g.CELLSIZE, g.CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.x = x
        self.y = y
        self.hitpoints = 1
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0
        self.facing = 0
        self.anicount = 0
        self.messages = ""
        self.has_key = 0

    def update(self, wallGroup, connGroup, bgGroup, message, coinGroup, keyGroup, doorGroup):
        global mapX, mapY
        current_x = self.x
        current_y = self.y
        if self.moving_down and self.y < (g.SCREENHEIGHT / g.CELLSIZE):
            self.y += 1
            self.anicount += 1
        if self.moving_up and self.y > 0:
            self.y -= 1
            self.anicount += 1
        if self.moving_right and self.x <= (g.SCREENWIDTH / g.CELLSIZE):
            self.x += 1
            self.anicount += 1
        if self.moving_left and self.x > 0:
            self.x -= 1
            self.anicount += 1
        if (self.x, self.y) in wallGroup:
            self.x = current_x
            self.y = current_y
        if (self.x, self.y) in connGroup:
            g.DISPLAYSURF.fill((0, 64, 0))

            if self.y >= ((g.SCREENHEIGHT / g.CELLSIZE) - 1) and self.moving_down:
                mapY += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup,
                             self, connGroup, coinGroup, keyGroup, doorGroup)
                self.y = 1
            elif self.x >= ((g.SCREENWIDTH / g.CELLSIZE) - 1) and self.moving_right:
                mapX += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup,
                             self, connGroup, coinGroup, keyGroup, doorGroup)
                self.x = 1
            elif self.y == 0 and self.moving_up:
                mapY -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup,
                             self, connGroup, coinGroup, keyGroup, doorGroup)
                self.y = 10
            elif self.x == 0 and self.moving_left:
                mapX -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup,
                             self, connGroup, coinGroup, keyGroup, doorGroup)
                self.x = 14
            if mapX == 0 and mapY == 1:
                message.update("Danger Ahead  (Press Space)!")
        if (self.x, self.y) in keyGroup:
            keyGroup.remove((self.x, self.y))
            self.has_key = 1

        if (self.x, self.y) in coinGroup:
            coinGroup.remove((self.x, self.y))

        if (self.x, self.y) in doorGroup and self.has_key == 1:
            doorGroup.remove((self.x, self.y))
            self.has_key = 0
        elif (self.x, self.y) in doorGroup:
            self.x = current_x
            self.y = current_y

        if self.x != current_x or self.y != current_y:
            g.NEXTMOVE = 1

        if self.anicount >= 3:
            self.anicount = 0
        self.moving_down = self.moving_up = self.moving_left = self.moving_right = 0

    def draw(self):
        if self.facing == 0:
            g.DISPLAYSURF.blit(
                self.player_img_right_list[self.anicount], (self.x * g.CELLSIZE / 2, self.y * g.CELLSIZE / 2))
        if self.facing == 1:
            g.DISPLAYSURF.blit(
                self.player_img_list[self.anicount], (self.x * g.CELLSIZE / 2, self.y * g.CELLSIZE / 2))
        if self.facing == 2:
            g.DISPLAYSURF.blit(
                self.player_img_left_list[self.anicount], (self.x * g.CELLSIZE / 2, self.y * g.CELLSIZE / 2))
        if self.facing == 3:
            g.DISPLAYSURF.blit(
                self.player_img_back_list[self.anicount], (self.x * g.CELLSIZE / 2, self.y * g.CELLSIZE / 2))
