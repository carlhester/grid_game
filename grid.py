import pygame
import sys
import random

CELLSIZE = 40 
SCREENWIDTH = 640
SCREENHEIGHT = 480
assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"



def main():
    global DISPLAYSURF, SCREENWIDTH, SCREENHEIGHT, CELLSIZE
    pygame.init()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    player = Player() 
    asteroidGroup = []
    asteroid = Asteroid()
    asteroidGroup.append(asteroid)

    running = True

    while running == True:
        DISPLAYSURF.fill((0, 0, 0))
        
        drawGrid()    
        for asteroid in asteroidGroup:
            asteroid.update()
            asteroid.draw()
        getInput(player)
        updatePlayer(player, SCREENWIDTH, SCREENHEIGHT, CELLSIZE)
        drawPlayer(player)
        pygame.display.update()



def drawGrid():
    for x in range(0, SCREENWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (x, 0), (x, SCREENHEIGHT))
    for y in range(0, SCREENHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (0, y), (SCREENWIDTH, y))

def drawPlayer(player):
    pygame.draw.rect(DISPLAYSURF, (255, 0, 255), (player.x * CELLSIZE, player.y * CELLSIZE, CELLSIZE, CELLSIZE))

def getInput(player):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.moving_down = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.moving_up = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.moving_right = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.moving_left = 1

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player.moving_down = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player.moving_up = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            player.moving_right = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            player.moving_left = 0



def updatePlayer(player, SCREENWIDTH, SCREENHEIGHT, CELLSIZE):
    if player.moving_down and player.y < (SCREENHEIGHT / CELLSIZE) - 1:
        player.y += 1
    if player.moving_up and player.y > 0:
        player.y -= 1
    if player.moving_right and player.x < (SCREENWIDTH / CELLSIZE) - 1:
        player.x += 1
    if player.moving_left and player.x > 0:
        player.x -= 1
        
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0

class Asteroid():
    def __init__(self):
        self.x = random.randint(0, (SCREENWIDTH / CELLSIZE) - 1)
        self.y = random.randint(0, (SCREENHEIGHT / CELLSIZE) - 1)
        print self.x, self.y

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, (128, 0, 255), (self.x * CELLSIZE, self.y * CELLSIZE, CELLSIZE, CELLSIZE))


if __name__ == '__main__':
    main()
