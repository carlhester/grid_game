
import sys
import time
import pygame
import levels
from levels import *
import globals as g


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
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

        self.hitpoints = 5
        self.coins = 1
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0
        self.facing = 0
        self.anicount = 0
        self.messages = ""
        self.has_key = 0
        self.rect = self.player_img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def input(self):
        for event in pygame.event.get():
            print(pygame.event.event_name(event.type))
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.moving_up = 0
                    self.moving_down = 1
                    self.facing = 1
                elif event.key == pygame.K_UP:
                    self.moving_down = 0
                    self.moving_up = 1
                    self.facing = 3
                elif event.key == pygame.K_RIGHT:
                    self.moving_left = 0
                    self.moving_right = 1
                    self.facing = 0
                elif event.key == pygame.K_LEFT:
                    self.moving_left = 1
                    self.moving_right = 0
                    self.facing = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.moving_down = 0
                elif event.key == pygame.K_UP:
                    self.moving_up = 0
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = 0
                elif event.key == pygame.K_LEFT:
                    self.moving_left = 0

    def update(self, blocker_sprites):
        if self.moving_right and self.rect.centerx <= (g.SCREENWIDTH):
            g.X_SCROLL -= 1
        elif self.moving_left and self.rect.centerx > 0:
            g.X_SCROLL += 1

        if self.moving_right | self.moving_left:
            self.collide("h", blocker_sprites)

        if self.moving_down and self.rect.centery < (g.SCREENHEIGHT):
            g.Y_SCROLL -= 1
        elif self.moving_up and self.rect.centery > 0:
            g.Y_SCROLL += 1

        for sprite in blocker_sprites:
            if sprite.rect.colliderect(self.rect) & self.moving_up:
                self.rect.top = sprite.rect.bottom
            elif sprite.rect.colliderect(self.rect) & self.moving_down:
                self.rect.bottom = sprite.rect.top

        self.anicount += 1
        if self.anicount >= 3:
            self.anicount = 0

    def collide(self, direction, blocker_sprites):
        if direction == "h":
            for sprite in blocker_sprites:
                if sprite.rect.colliderect(self.rect) & self.moving_right:
                    self.rect.right = sprite.rect.left
                elif sprite.rect.colliderect(self.rect) & self.moving_left:
                    self.rect.left = sprite.rect.right

    def draw(self):
        if self.facing == 0:
            g.DISPLAYSURF.blit(
                self.player_img_right_list[self.anicount], (self.rect.x*g.CELLSIZE, self.rect.y*g.CELLSIZE))
        if self.facing == 1:
            g.DISPLAYSURF.blit(
                self.player_img_list[self.anicount], (self.rect.x*g.CELLSIZE, self.rect.y*g.CELLSIZE))
        if self.facing == 2:
            g.DISPLAYSURF.blit(
                self.player_img_left_list[self.anicount], (self.rect.x*g.CELLSIZE, self.rect.y*g.CELLSIZE))
        if self.facing == 3:
            g.DISPLAYSURF.blit(
                self.player_img_back_list[self.anicount], (self.rect.x*g.CELLSIZE, self.rect.y*g.CELLSIZE))
