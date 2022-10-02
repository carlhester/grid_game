import pygame
import globals as g
import sys


class Input():
    def __init__(self):
        self.x_scroll = 0
        self.y_scroll = 0

    def update(self, camera):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            # print(pygame.event.event_name(event.type))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.y_scroll = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.x_scroll = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y_scroll = 1
                elif event.key == pygame.K_DOWN:
                    self.y_scroll = -1

                if event.key == pygame.K_LEFT:
                    self.x_scroll = 1
                elif event.key == pygame.K_RIGHT:
                    self.x_scroll = -1
            print(self.x_scroll, self.y_scroll)

        camera.update(self.x_scroll, self.y_scroll)
