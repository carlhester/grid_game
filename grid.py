import pygame
from camera import Camera
import globals as g
from player import *
from pygame.locals import *
from room import *
from input import *


def main():
    g = Game()
    g.run()


class Game:
    def __init__(self):
        pygame.init()
        self.camera = Camera()

    def run(self):
        FPSCLOCK = pygame.time.Clock()

        g.DISPLAYSURF = pygame.display.set_mode(
            (g.SCREENWIDTH, g.SCREENHEIGHT))

        room = Room(self.camera)
        # player = Player(3, 3)
        game_input = Input()

        GAMERUNNING = True
        while GAMERUNNING == True:
            g.DISPLAYSURF.fill(g.BLACK)
            # msg = str(int(FPSCLOCK.get_fps())) + " fps " + \
            #     "\t" + str(g.Y_OFFSET) + ":" + str(g.X_OFFSET) + " -- " + \
            #     str(player.moving_up) + ":" + str(player.moving_down) + ":" + \
            #     str(player.moving_left) + ":" + str(player.moving_right) + "--" + \
            #     str(player.rect)
            # print(msg)

            game_input.update(self.camera)
            # player.input()

            room.update()
            room.draw(self.camera)
            # player.draw()
            # drawGrid()
            # drawHearts(player)
            # drawCoins(player)
            pygame.display.update()
            FPSCLOCK.tick(g.FPS)


def drawHearts(player):
    heart_img = pygame.image.load('images/heart.png')
    heart_img = pygame.transform.scale(heart_img, (20, 20))
    spacing = 10
    if player.hitpoints > 0:
        for heart in range(1, player.hitpoints + 1):
            g.DISPLAYSURF.blit(heart_img, (spacing, 10))
            spacing += 30


def drawCoins(player):
    coin_img = pygame.image.load('images/coin.png')
    coin_img = pygame.transform.scale(coin_img, (20, 20))
    spacing = 10
    if player.hitpoints > 0:
        for coin in range(1, player.coins + 1):
            g.DISPLAYSURF.blit(coin_img, (spacing+200, 10))
            spacing += 10


def drawGrid():
    for x in range(0, g.SCREENWIDTH, g.CELLSIZE):
        pygame.draw.line(g.DISPLAYSURF, (100, 100, 100),
                         (x, 0), (x, g.SCREENHEIGHT))
    for y in range(0, g.SCREENHEIGHT, g.CELLSIZE):
        pygame.draw.line(g.DISPLAYSURF, (100, 100, 100),
                         (0, y), (g.SCREENWIDTH, y))


# def getInput(player):
if __name__ == '__main__':
    main()
