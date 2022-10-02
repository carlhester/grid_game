import pygame
import globals as g


class Camera():
    def __init__(self):
        self.X_OFFSET = 0
        self.Y_OFFSET = 0
        self.width = 0
        self.height = 0

    def update(self, x_scroll, y_scroll):
        self.X_OFFSET += x_scroll
        if self.X_OFFSET > 0:
            self.X_OFFSET = 0
        if self.X_OFFSET <= -self.width:
            self.X_OFFSET = -self.width

        self.Y_OFFSET += y_scroll
        if self.Y_OFFSET > 0:
            self.Y_OFFSET = 0
        if self.Y_OFFSET <= -self.height:
            self.Y_OFFSET = -self.height

    def set_width(self, width):
        self.width = -width

    def set_height(self, height):
        self.height = -height
