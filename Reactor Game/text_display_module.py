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


    def power_round_recursion(self, input_int, depth):
        suffix_list = [" W", " kW", " mW", " gW"]
        if input_int > 100000:
            input_int /= 1000
            return self.power_round_recursion(input_int, depth+1)
        return str(int(input_int)) + suffix_list[depth]

    def draw(self):
        suffix = ""
        if self.special == "round":
            display_value = round(self.value, 3)
        else:
            display_value = int(self.value)
            if self.special == "power_round":
                display_value = self.power_round_recursion(display_value, 0)        #visual starting power suffix

        value_font = pygame.font.SysFont("comicsansms", 24)
        value_display = value_font.render(self.title + str(display_value) + suffix, True, (0,0,0))
        self.screen.blit(value_display, (self.x, self.y))