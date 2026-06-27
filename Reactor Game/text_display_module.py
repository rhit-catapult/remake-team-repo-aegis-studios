import pygame

class Text_Display():

    def __init__(self, screen, x, y, title, special = "regular"):
        self.screen = screen
        self.x = x
        self.y = y
        self.title = title
        self.value = 0
        self.special = special

    def set_value(self, value):
        self.value = value

    def draw(self):
        suffix = ""
        if self.special == "round":
            display_value = round(self.value, 3)
        else:
            display_value = int(self.value)
            if self.special == "power_round":
                display_value = display_value / 100
                display_value = int(display_value)
                display_value = display_value / 10
                suffix = "gW"

        value_font = pygame.font.SysFont("comicsansms", 24)
        value_display = value_font.render(self.title + str(display_value) + suffix, True, (0,0,0))
        self.screen.blit(value_display, (self.x, self.y))