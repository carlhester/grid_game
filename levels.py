from levels import *
import globals as g
from tile import *


class Level():
    def __init__(self, level):
        pass

    def draw(self):
        pass


def draw_level(drawGroup):
    for tile in drawGroup:
        tile.draw(g.DISPLAYSURF)
        # if bg_type == '#':
        # g.DISPLAYSURF.blit(bg_images['wall'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == 'D' and (x, y) in doorGroup:
        #     g.DISPLAYSURF.blit(bg_images['door'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == 'C' and (x, y) in coinGroup:
        #     g.DISPLAYSURF.blit(bg_images['coin'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == 'k' and (x, y) in keyGroup:
        #     g.DISPLAYSURF.blit(
        #         bg_images['key'], (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == '0':
        #     g.DISPLAYSURF.blit(bg_images['rock1'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == 'O':
        #     g.DISPLAYSURF.blit(bg_images['rock2'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == 'o':
        #     g.DISPLAYSURF.blit(bg_images['rock3'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))
        # elif bg_type == '*' or bg_type == 'X':
        #     g.DISPLAYSURF.blit(bg_images['sand'],
        #                        (x * g.CELLSIZE, y * g.CELLSIZE))


# def create_room(level, bgGroup, wallGroup, player, connGroup, coinGroup, keyGroup, doorGroup):
#     block_items = ["#", "o", "O", "0"]
#     for y in range(0, len(level)):
#         for x in range(0, len(level[y])):
#             wallGroup.append(Tile(x, y, level[y][x]))
#         # if level[y][x] == 'X':
#         #     connGroup.append((x, y))
#         # if level[y][x] == 'C':
#         #     coinGroup.append((x, y))
#         # if level[y][x] == 'k':
#         #     keyGroup.append((x, y))
#         # if level[y][x] == 'D':
#         #     doorGroup.append((x, y))


w, h = 3, 3
levels = [[0 for x in range(w)] for y in range(h)]

levels[0][0] = ["################",
                "##.#...........#",
                "#.............*X",
                "#...........***X",
                "#.C............#",
                "#..............#",
                "#...o......oo..#",
                "O...O##....o...#",
                "oo..0..........#",
                "o0O............#",
                "Oo0.......##...#",
                "0oo###XX########"]

levels[1][0] = ["################",
                "#.#............#",
                "X..............#",
                "X........###...#",
                "#..............#",
                "#..............#",
                "#..............#",
                "#....##........X",
                "#..............X",
                "#..CC..........#",
                "#..............#",
                "######XX########"]

levels[2][0] = ["################",
                "####......##...#",
                "###............#",
                "###............#",
                "#.##...........#",
                "###............#",
                "#.#ooO.........#",
                "X....##........#",
                "X..............#",
                "#...C..........#",
                "#..........#####",
                "######XX########"]

levels[2][1] = ["######XX########",
                "#..#...........#",
                "X..............#",
                "X........##....#",
                "#..............#",
                "#.........##.###",
                "#..............#",
                "#....##........#",
                "#..............#",
                "#..............#",
                "#...........##.#",
                "######XX########"]

levels[0][1] = ["######XX########",
                "#..............#",
                "##.............X",
                "#.........##...X",
                "#..............#",
                "#..............#",
                "#..#..#........#",
                "#..####......###",
                "#............###",
                "#..............#",
                "#..............#",
                "######XX########"]

levels[0][2] = ["######XX########",
                "#..............#",
                "#..............X",
                "##........##...X",
                "#..............#",
                "#..............#",
                "#..............#",
                "#...###........#",
                "#...#..........#",
                "#....#.........#",
                "#.....#........#",
                "################"]

levels[1][1] = ["######XX########",
                "#..............#",
                "X.#............X",
                "X.........##...X",
                "#..............#",
                "#..............#",
                "#..............#",
                "#....##........#",
                "#..............#",
                "#..............#",
                "####......##...#",
                "######XX########"]

levels[1][2] = ["#######XX#######",
                "#..............#",
                "X..............#",
                "X.#.......##...#",
                "#..............#",
                "#..............X",
                "#..........###.X",
                "#....##......#.#",
                "#..............#",
                "#..............#",
                "##..........##.#",
                "################"]

levels[2][2] = ["#######XX#######",
                "#.............k#",
                "#..............#",
                "#..#......##...#",
                "#.........##...#",
                "X..........#...#",
                "X..............#",
                "#....##D###....#",
                "#....#C..C#....#",
                "#....#CCCC######",
                "#....#CCCC#...##",
                "################"]
