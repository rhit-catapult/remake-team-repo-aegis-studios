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
        if self.special == "temp":
            display_value = int(self.value)
            suffix = " K"
        elif self.special == "temp_round":
            display_value = round(self.value, 3)
            suffix = " K"
        elif self.special == "pressure":
            display_value = int(self.value)
            suffix = " PSI"
        elif self.special == "pressure_round":
            display_value = round(self.value, 3)
            suffix = " PSI"
        elif self.special == "power_round":
            display_value = self.value
            display_value = display_value * 10
            display_value = int(display_value)
            display_value = display_value / 10
            suffix = " GW"
        elif self.special == "time_left":
            display_value = int(self.value)
            suffix = " s"
        else:
            display_value = int(self.value)

        value_font = pygame.font.SysFont("calibri", 16)
        value_display = value_font.render(self.title + str(display_value) + suffix, True, (255,255,255))
        self.screen.blit(value_display, (self.x, self.y))