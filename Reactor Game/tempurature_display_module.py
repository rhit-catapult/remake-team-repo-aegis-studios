import pygame

class Tempurature():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def set_value(self, temp):
        self.temp = temp

    def draw(self):
        temp_font = pygame.font.SysFont("comicsansms", 24)
        temp_display = temp_font.render(str(int(self.temp)), True, (0,0,0))
        self.screen.blit(temp_display, (self.x, self.y))