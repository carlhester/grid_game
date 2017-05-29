import pygame
import sys
import random
import levels
from pygame.locals import *

FPS = 30
CELLSIZE = 50 
SCREENWIDTH = 800
SCREENHEIGHT = 600

assert SCREENWIDTH % CELLSIZE == 0, "dimensions are off"
assert SCREENHEIGHT % CELLSIZE == 0, "dimensions are off"

def main():
    global GAMERUNNING, FPSCLOCK, DISPLAYSURF, SCREENWIDTH, SCREENHEIGHT, CELLSIZE, mapX, mapY, NEXTMOVE
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    basicfont = pygame.font.SysFont(None, 32, 0, 1)
   
    bg_images = generate_map_images()
    NEXTMOVE = 0

    player = Player(5,4) 
    badguy = BadGuy(5, 5, "shyguy")

    mapX = 0
    mapY = 0 
    wallGroup = [] 
    bgGroup = []
    connGroup = []
    shotGroup = []
    message = Message()
    create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, player, connGroup)
    
    GAMERUNNING = True
    while GAMERUNNING == True:
        pygame.display.set_caption(str(player.x) + ":" + str(player.y) + "\t" + str(mapX) + ":" + str(mapY)) 
        draw_level(bgGroup, bg_images)
        getInput(player, message, shotGroup)
        player.update(wallGroup, connGroup, bgGroup, message)
        badguy.update(wallGroup)
        NEXTMOVE = 0 
        badguy.draw()
        player.draw()
        #drawGrid()    
        for shot in shotGroup:
            shot.update(shotGroup)
            shot.draw()
        drawHearts(player)
        message.draw(basicfont)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def brickClearScreen():
    # this doesn't work on OSX :(
    global DISPLAYSURF
    width = 30
    height = 10
    DISPLAYSURF.fill((255, 255, 255))
    pygame.display.update()
    for x in range(0, SCREENWIDTH, width):
        for y in range(0, SCREENHEIGHT, height):
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (x, y, width, height))
            pygame.display.update()

class Shot():
    def __init__(self, player):
        self.shot_img = pygame.image.load('shot.png')
        self.shot_img = pygame.transform.scale(self.shot_img, (CELLSIZE, CELLSIZE))
        self.shot_img_up = pygame.transform.rotate(self.shot_img, -90)
        self.shot_img_down = pygame.transform.rotate(self.shot_img, 90)
        self.shot_img_right = pygame.transform.flip(self.shot_img, 1, 0)
        self.facing = player.facing
        self.speed = 30
        self.x = player.x * CELLSIZE
        self.y = player.y * CELLSIZE
       
    def update(self, shotGroup):
        if self.y > SCREENHEIGHT or self.y < 0 or self.x > SCREENWIDTH or self.x < 0:
            shotGroup.remove(self)
            
        if self.facing == 1 and self.y <= SCREENHEIGHT:
            self.y += self.speed
        elif self.facing == 3 and self.y >= -5:
            self.y -= self.speed
        elif self.facing == 0 and self.x <= SCREENWIDTH:
            self.x += self.speed
        elif self.facing == 2 and self.x > -5:
            self.x -= self.speed
        
    
             
    def draw(self): 
        if self.facing == 1: self.shot_img = self.shot_img_down
        if self.facing == 0: self.shot_img = self.shot_img_right
        if self.facing == 3: self.shot_img = self.shot_img_up
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
            width = int(SCREENWIDTH * .8)
            height = int(SCREENHEIGHT / 5)
            left = int(SCREENWIDTH - width) / 2
            top = int((SCREENHEIGHT / 5))
            textlength = len(self.text)
            pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (left, top, width, height))
            text = basicfont.render(self.text, False, (255, 255, 255), (0,0,0))
            textrect = text.get_rect()
            textrect.centerx = left + (((width) / 2) - (textlength/2))
            textrect.y = top + (height / 2)
            DISPLAYSURF.blit(text, textrect)
    
    def clear(self):
        self.text = ""

 
def drawHearts(player):
    heart_img = pygame.image.load('heart.png')
    heart_img = pygame.transform.scale(heart_img, (20, 20))
    spacing = 10
    if player.hitpoints > 0:
        for heart in range(1, player.hitpoints + 1):
            DISPLAYSURF.blit(heart_img, (spacing, 10))
            spacing += 30

def create_level(level, bgGroup, wallGroup, player, connGroup):
    block_items = ["#", "o", "O", "0"] 
    for y in range(0, len(level)):
        for x in range(0, len(level[y])):
            bgGroup.append((x, y, level[y][x]))
            if level[y][x] in block_items:
                wallGroup.append((x, y))
            if level[y][x] == 'X':
                connGroup.append((x, y))

def draw_level(bgGroup, bg_images):
    for x, y, bg_type in bgGroup:
        DISPLAYSURF.blit(bg_images['grass'], (x * CELLSIZE, y * CELLSIZE))
        if bg_type == '#':
            DISPLAYSURF.blit(bg_images['wall'], (x * CELLSIZE, y * CELLSIZE))
        elif bg_type == '0':
            DISPLAYSURF.blit(bg_images['rock1'], (x * CELLSIZE, y * CELLSIZE))
        elif bg_type == 'O':
            DISPLAYSURF.blit(bg_images['rock2'], (x * CELLSIZE, y * CELLSIZE))
        elif bg_type == 'o':
            DISPLAYSURF.blit(bg_images['rock3'], (x * CELLSIZE, y * CELLSIZE))
        elif bg_type == '*' or bg_type == 'X':
            DISPLAYSURF.blit(bg_images['sand'], (x * CELLSIZE, y * CELLSIZE))
        #else:
        #    DISPLAYSURF.blit(bg_images['grass'], (x * CELLSIZE, y * CELLSIZE))


def drawGrid():
    for x in range(0, SCREENWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (x, 0), (x, SCREENHEIGHT))
    for y in range(0, SCREENHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (0, y), (SCREENWIDTH, y))


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
        self.badguy_img = pygame.image.load('badguy.png')
        self.badguy_img = pygame.transform.scale(self.badguy_img, (CELLSIZE, CELLSIZE))
        self.x = x
        self.y = y
        self.badguytype = badguytype
        self.moving_direction = 0
        self.distance_traveled = 0 

    def update(self, wallGroup):
        global NEXTMOVE
        if NEXTMOVE == 1:
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
                self.moving_direction = random.randint(0,4) 
            if (self.x, self.y) in wallGroup:
                self.x = current_x
                self.y = current_y

    def draw(self):
        DISPLAYSURF.blit(self.badguy_img, (self.x * CELLSIZE, self.y * CELLSIZE))


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


    def update(self, wallGroup, connGroup, bgGroup, message):
        global mapX, mapY, NEXTMOVE
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
            DISPLAYSURF.fill((0, 64, 0))
            
            if self.y >= ((SCREENHEIGHT / CELLSIZE) - 1) and self.moving_down:
                mapY += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.y = 1
            elif self.x >= ((SCREENWIDTH / CELLSIZE) - 1) and self.moving_right:
                mapX += 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.x = 1
            elif self.y == 0 and self.moving_up:
                mapY -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.y = 10
            elif self.x == 0 and self.moving_left:
                mapX -= 1
                del bgGroup[:]
                del wallGroup[:]
                del connGroup[:]
                create_level(levels.levels[mapX][mapY], bgGroup, wallGroup, self, connGroup)
                self.x = 14
            if mapX == 0 and mapY == 1: 
                message.update("Danger Ahead  (Press Space)!")
      
        if self.x != current_x or self.y != current_y:
                NEXTMOVE = 1
                
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



def generate_map_images():
    grass_img = pygame.image.load('grass.png')
    grass_img = pygame.transform.scale(grass_img, ((CELLSIZE, CELLSIZE)))
    wall_img = pygame.image.load('wall.png')
    wall_img = pygame.transform.scale(wall_img, ((CELLSIZE, CELLSIZE)))
    sand_img = pygame.image.load('sand.png')
    sand_img = pygame.transform.scale(sand_img, ((CELLSIZE, CELLSIZE)))

    rock_spritesheet = pygame.image.load('rock_spritesheet.png')
    rock_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
    rock_surf.blit(rock_spritesheet, (-70, 0))
    rock1_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))
    rock_surf.blit(rock_spritesheet, (-35, 0))
    rock2_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))
    rock_surf.blit(rock_spritesheet, (0, 0))
    rock3_img = pygame.transform.scale(rock_surf, (CELLSIZE, CELLSIZE))

    bg_images = {}
    bg_images = {'grass' : grass_img, 'wall' : wall_img, 'rock1' : rock1_img, 'rock2' : rock2_img, 'rock3' : rock3_img, 'sand' : sand_img}
    return bg_images
 

if __name__ == '__main__':
    main()
