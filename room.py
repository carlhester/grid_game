import pygame
from tile import *


class Room():
    def __init__(self, camera):
        self.visible_tiles = pygame.sprite.Group()
        self.blocker_tiles = pygame.sprite.Group()

        for y in range(0, len(room)):
            for x in range(0, len(room[y])):
                self.visible_tiles.add(Tile(x, y, room[y][x]))
                if room[y][x] == "#":
                    self.blocker_tiles.add(Tile(x, y, room[y][x]))

        camera.set_height((g.SCREENHEIGHT/g.CELLSIZE) - len(room))
        camera.set_width((g.SCREENWIDTH/g.CELLSIZE) - len(room[0]))

    def get_blocker_sprites(self):
        return self.blocker_tiles

    def update(self):
        for tile in self.visible_tiles:
            tile.update()

    def draw(self, camera):
        for tile in self.visible_tiles:
            tile.draw(camera)


room = ["######################################",
        "#................#................#.##",
        "#...............#.................#.##",
        "#..#...........#..................#.##",
        "#...#.........#...................#.##",
        "#....#........#...................#.##",
        "#....#........#...................#.##",
        "#....#........#...................#.##",
        "#....#........#...................#.##",
        "#....#........#...................#.##",
        "#.............#...................#.##",
        "#.............#...................#.##",
        "#.............#...................#.##",
        "#.............#...................#.##",
        "#.............#...................#.##",
        "#............#....................#.##",
        "#.................................#.##",
        "######################################"]
