import pygame

class Text_Display():

    def __init__(self, screen, x, y, title, decimal=False):
        self.screen = screen
        self.x = x
        self.y = y
        self.title = title
        self.value = 0
        self.decimal = decimal

    def set_value(self, value):
        self.value = value

    def draw(self):
        if self.decimal:
            self.display_value = round(self.value, 3)
        else:
            self.display_value = int(self.value)
        value_font = pygame.font.SysFont("comicsansms", 24)
        value_display = value_font.render(self.title + str(self.display_value), True, (0,0,0))
        self.screen.blit(value_display, (self.x, self.y))