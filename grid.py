import pygame
import sys
import random

FPS = 30 
CELLSIZE = 50 
SCREENWIDTH = 800
SCREENHEIGHT = 600
assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"


def main():
    global FPSCLOCK, DISPLAYSURF, SCREENWIDTH, SCREENHEIGHT, CELLSIZE
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    player = Player() 
#    asteroidGroup = []
#    while len(asteroidGroup) < 5:
#        asteroid = Asteroid()
#        asteroidGroup.append(asteroid)

    running = True

    while running == True:
        DISPLAYSURF.fill((0, 0, 0))
        
        drawGrid()    
        #for asteroid in asteroidGroup:
        #    asteroid.update()
        #    asteroid.draw()
        getInput(player)
        player.update()
        player.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def drawGrid():
    for x in range(0, SCREENWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (x, 0), (x, SCREENHEIGHT))
    for y in range(0, SCREENHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (0, y), (SCREENWIDTH, y))

def getInput(player):
    for event in pygame.event.get():
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
            player.facing = 1 

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player.moving_down = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player.moving_up = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            player.moving_right = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            player.moving_left = 0

class Player():
    def __init__(self):
        self.player_surf = pygame.Surface((CELLSIZE, CELLSIZE), pygame.SRCALPHA).convert()
        self.player_rect = self.player_surf.get_rect()
        self.player_img = pygame.image.load('hero.png')
        self.player_img = pygame.transform.scale(self.player_img, (CELLSIZE, CELLSIZE))
        self.player_rect = self.player_img.get_rect()

        self.player_img_back = pygame.image.load('hero_back.png')
        self.player_img_back = pygame.transform.scale(self.player_img_back, (CELLSIZE, CELLSIZE))
        self.player_rect = self.player_img_back.get_rect()

        self.x = 0
        self.y = 0
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0
        self.facing = 0 


    def update(self):
        if self.moving_down and self.y < (SCREENHEIGHT / CELLSIZE) - 1:
            self.y += 1
        if self.moving_up and self.y > 0:
            self.y -= 1
        if self.moving_right and self.x < (SCREENWIDTH / CELLSIZE) - 1:
            self.x += 1
        if self.moving_left and self.x > 0:
            self.x -= 1

    def draw(self):
        #pygame.draw.rect(DISPLAYSURF, (255, 0, 255), (self.x * CELLSIZE, self.y * CELLSIZE, CELLSIZE, CELLSIZE))
        if self.facing == 3:
            DISPLAYSURF.blit(self.player_img_back, (self.x * CELLSIZE,self.y * CELLSIZE))
        else:
            DISPLAYSURF.blit(self.player_img, (self.x * CELLSIZE,self.y * CELLSIZE))
        

class Asteroid():
    def __init__(self):
        self.x = random.randint(0, (SCREENWIDTH / CELLSIZE) - 1)
        self.y = random.randint(0, (SCREENHEIGHT / CELLSIZE) - 1)

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, (128, 0, 255), (self.x * CELLSIZE, self.y * CELLSIZE, CELLSIZE, CELLSIZE))


if __name__ == '__main__':
    main()
