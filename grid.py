import pygame
import sys
import random
import levels

FPS = 30
CELLSIZE = 50 
SCREENWIDTH = 800
SCREENHEIGHT = 600

assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"

def main():
    global GAMERUNNING, FPSCLOCK, DISPLAYSURF, SCREENWIDTH, SCREENHEIGHT, CELLSIZE, mapX, mapY
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    DISPLAYSURF.set_alpha(0)
   
    grass_img = pygame.image.load('grass.png')
    grass_img = pygame.transform.scale(grass_img, ((CELLSIZE, CELLSIZE)))
    wall_img = pygame.image.load('wall.png')
    wall_img = pygame.transform.scale(wall_img, ((CELLSIZE, CELLSIZE)))

    bg_images = {}
    bg_images = {'grass' : grass_img, 'wall' : wall_img}

    player = Player(5,4) 

    mapX = 0
    mapY = 0 
    wallGroup = [] 
    bgGroup = []
    connGroup = []
    create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, player, connGroup)
    
    GAMERUNNING = True
    while GAMERUNNING == True:
        pygame.display.set_caption(str(player.x) + ":" + str(player.y) + "\t" + str(mapX) + ":" + str(mapY)) 
        drawMessages()
        getInput(player)
        player.update(wallGroup, connGroup, bgGroup)
        draw_level(bgGroup, bg_images)
        player.draw()
        #drawGrid()    
        drawHearts(player)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawHearts(player):
    heart_img = pygame.image.load('heart.png')
    heart_img = pygame.transform.scale(heart_img, (20, 20))
    spacing = 10
    if player.hitpoints > 0:
        for heart in range(1, player.hitpoints + 1):
            DISPLAYSURF.blit(heart_img, (spacing, 10))
            spacing += 30

def drawMessages(message=False):
    if message != "":
        width = int(SCREENWIDTH * .8)
        height = int(SCREENHEIGHT / 5)
        left = int(SCREENWIDTH - width) / 2
        top = int((SCREENHEIGHT / 5))
        pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (left, top, width, height))
    
def create_level(level, bgGroup, wallGroup, player, connGroup):
    for y in range(0, len(level)):
        for x in range(0, len(level[y])):
            bgGroup.append((x, y, level[y][x]))
            if level[y][x] == '#':
                wallGroup.append((x, y))
            if level[y][x] == 'X':
                connGroup.append((x, y))

def draw_level(bgGroup, bg_images):
    for x, y, bg_type in bgGroup:
        if bg_type == '#':
            DISPLAYSURF.blit(bg_images['wall'], (x * CELLSIZE, y * CELLSIZE))
        else:
            DISPLAYSURF.blit(bg_images['grass'], (x * CELLSIZE, y * CELLSIZE))


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

class Player():
    def __init__(self, x, y):

        self.spritesheet = pygame.image.load('hero_spritesheet.png')     
   
        self.player_img_list = [] 
        self.player_img_back_list = [] 
        self.player_img_right_list = [] 
        self.player_img_left_list = [] 

        #walking down
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
        
        #walking up
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        #walking right 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        #walking left 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-32, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (0, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.player_surf.blit(self.spritesheet, (-64, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
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


    def update(self, wallGroup, connGroup, bgGroup):
        global mapX, mapY 
        current_x = self.x
        current_y = self.y
        if self.moving_down and self.y < (SCREENHEIGHT / CELLSIZE):
            self.y += 1
            self.anicount += 1
        if self.moving_up and self.y > 0:
            self.y -= 1
            self.anicount += 1
        if self.moving_right and self.x <= (SCREENWIDTH / CELLSIZE):
            self.x += 1
            self.anicount += 1
        if self.moving_left and self.x > 0:
            self.x -= 1
            self.anicount += 1
        if (self.x, self.y) in wallGroup:
            self.x = current_x
            self.y = current_y 
        if (self.x, self.y) in connGroup:
            if self.y >= ((SCREENHEIGHT / CELLSIZE) - 1) and self.moving_down:
                mapY += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.y = 0
            elif self.x >= ((SCREENWIDTH / CELLSIZE) - 1) and self.moving_right:
                mapX += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.x = 0
            elif self.y == 0 and self.moving_up:
                mapY -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.y = 11
            elif self.x == 0 and self.moving_left:
                mapX -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.x = 15
        if self.anicount >= 3:
            self.anicount = 0
        self.moving_down = self.moving_up = self.moving_left = self.moving_right = 0     


    def draw(self):
        if self.facing == 0:
            DISPLAYSURF.blit(self.player_img_right_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 1:
            DISPLAYSURF.blit(self.player_img_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 2:
            DISPLAYSURF.blit(self.player_img_left_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 3:
            DISPLAYSURF.blit(self.player_img_back_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))

 

if __name__ == '__main__':
    main()
