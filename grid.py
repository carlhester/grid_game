import pygame
import sys


CELLWIDTH = 40 

def main():
    global DISPLAYSURF

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((640, 480))
    running = True

    while running == True:
        DISPLAYSURF.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        drawGrid()    

        pygame.display.update()

def drawGrid():
    for x in range(0, 640, CELLWIDTH):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (x, 0), (x, 480))
    for y in range(0, 480, CELLWIDTH):
        pygame.draw.line(DISPLAYSURF, (100, 100, 100), (0, y), (640, y))




if __name__ == '__main__':
    main()
