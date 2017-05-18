import pygame
import sys


CELLSIZE = 10 
SCREENWIDTH = 640
SCREENHEIGHT = 480
assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"



def main():
    global DISPLAYSURF
    pygame.init()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    player = Player() 
    running = True

    while running == True:
        DISPLAYSURF.fill((0, 0, 0))
        
        drawGrid()    
        getInput(player)
        updatePlayer(player)
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.moving_down = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.moving_up = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.moving_right = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.moving_left = 1

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player.moving_down = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player.moving_up = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            player.moving_right = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            player.moving_left = 0



def updatePlayer(player):
    if player.moving_down:
        player.y += 1
    if player.moving_up:
        player.y -= 1
    if player.moving_right:
        player.x += 1
    if player.moving_left:
        player.x -= 1
        
class Player():
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0


if __name__ == '__main__':
    main()
