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
    global FPSCLOCK, DISPLAYSURF, SCREENWIDTH, SCREENHEIGHT, CELLSIZE
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    player = Player() 

    wallGroup = [] 
    bgGroup = []
    create_level(levels.levels[0][0], bgGroup, wallGroup)
    running = True
    
    while running == True:
        DISPLAYSURF.fill((0, 0, 0))
        getInput(player)
        player.update(wallGroup)
        draw_level(bgGroup)
        player.draw()
        #drawGrid()    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def create_level(level, bgGroup, wallGroup):
    for y in range(0, len(level)):
        for x in range(0, len(level[y])):
            bgGroup.append((x, y, level[y][x]))
            if level[y][x] == '#':
                wallGroup.append((x, y))

def draw_level(bgGroup):
    grass_img = pygame.image.load('grass.png')
    grass_img = pygame.transform.scale(grass_img, ((CELLSIZE, CELLSIZE)))
    wall_img = pygame.image.load('wall.png')
    wall_img = pygame.transform.scale(wall_img, ((CELLSIZE, CELLSIZE)))

    for x, y, bg_type in bgGroup:
        if bg_type == '#':
            DISPLAYSURF.blit(wall_img, (x * CELLSIZE, y * CELLSIZE))
        if bg_type == '.':
            DISPLAYSURF.blit(grass_img, (x * CELLSIZE, y * CELLSIZE))


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

        self.spritesheet = pygame.image.load('hero_spritesheet.png')     
   
        self.player_img_list = [] 
        self.player_img_back_list = [] 
        self.player_img_right_list = [] 
        self.player_img_left_list = [] 

        #walking down
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-32, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (0, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-64, 0))
        self.player_img = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_list.append(self.player_img)
        
        #walking up
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-32, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (0, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-64, -96))
        self.player_img_back = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_back_list.append(self.player_img_back)
        
        #walking right 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-32, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (0, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-64, -64))
        self.player_img_right = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_right_list.append(self.player_img_right)
       
        #walking left 
        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-32, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (0, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)

        self.player_surf = pygame.Surface((30, 30), pygame.SRCALPHA).convert()
        self.player_surf.blit(self.spritesheet, (-64, -32))
        self.player_img_left = pygame.transform.scale(self.player_surf, (CELLSIZE, CELLSIZE))
        self.player_img_left_list.append(self.player_img_left)


        self.x = 5
        self.y = 4
        self.moving_down = 0
        self.moving_up = 0
        self.moving_left = 0
        self.moving_right = 0
        self.facing = 0 
        self.anicount = 0


    def update(self, wallGroup):
        current_x = self.x
        current_y = self.y
        if self.moving_down and self.y < (SCREENHEIGHT / CELLSIZE) - 1:
            self.y += 1
            self.anicount += 1
        if self.moving_up and self.y > 0:
            self.y -= 1
            self.anicount += 1
        if self.moving_right and self.x < (SCREENWIDTH / CELLSIZE) - 1:
            self.x += 1
            self.anicount += 1
        if self.moving_left and self.x > 0:
            self.x -= 1
            self.anicount += 1
        if (self.x, self.y) in wallGroup:
            self.x = current_x
            self.y = current_y 
        pygame.time.wait(100)
        if self.anicount >= 3:
            self.anicount = 0
            


    def draw(self):
        if self.facing == 0:
            DISPLAYSURF.blit(self.player_img_right_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 1:
            DISPLAYSURF.blit(self.player_img_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 2:
            DISPLAYSURF.blit(self.player_img_left_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))
        if self.facing == 3:
            DISPLAYSURF.blit(self.player_img_back_list[self.anicount], (self.x * CELLSIZE,self.y * CELLSIZE))

 
class Wall():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.draw_image = False

        self.wall_img = pygame.image.load('wall.png')
        self.wall_img = pygame.transform.scale(self.wall_img, ((CELLSIZE, CELLSIZE)))
 
        self.grass_img = pygame.image.load('grass.png')
        self.grass_img = pygame.transform.scale(self.wall_img, ((CELLSIZE, CELLSIZE)))


    def update(self):
        pass
        
    def draw(self, bg_type, x, y):
        if bg_type == '#':
            self.draw_img = self.wall_img
        elif bg_type == '.':
            self.draw_image = self.grass_img
        else:
            self.draw_image = self.grass_img
        
        DISPLAYSURF.blit(self.draw_img, (self.x * CELLSIZE, self.y * CELLSIZE))
         

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
