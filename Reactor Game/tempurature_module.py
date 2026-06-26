import pygame


class Tempurature():

    def __init__(self, screen, x, y, start_temp, heat_levers, cool_levers):
        self.screen = screen
        self.x = x
        self.y = y
        self.temp = start_temp
        self.heat_levers = heat_levers
        self.cool_levers = cool_levers

    def set_temp(self):
        self.temp = int(input("Set Tempurature: "))

    def get_temp(self):
        return self.temp

    def update_values(self):
        reduction_factor = 100 #to balance the game
        for heat_lever in self.heat_levers:
            self.temp += (heat_lever.get_position() + 1) / reduction_factor
        for cool_lever in self.cool_levers:
            self.temp -= (cool_lever.get_position() *2)  / reduction_factor

    def draw(self):
        temp_font = pygame.font.SysFont("comicsansms", 24)
        temp_display = temp_font.render(str(int(self.temp)), True, (0,0,0))
        self.screen.blit(temp_display, (self.x, self.y))