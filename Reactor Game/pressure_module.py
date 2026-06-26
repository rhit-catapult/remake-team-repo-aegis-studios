import pygame

class Pressure():

    def __init__(self, screen, x, y, start_pressure, heat_levers, vent_buttons, tempurature_display):
        self.screen = screen
        self.x = x
        self.y = y
        self.pressure = start_pressure
        self.heat_levers = heat_levers
        self.vent_buttons = vent_buttons
        self.tempurature_display = tempurature_display

    def set_pressure(self):
        self.pressure = int(input("Set Pressure: "))

    def update_values(self):
        reduction_factor = 33 #to balance the game
        for heat_lever in self.heat_levers:
            self.pressure += ((heat_lever.get_position() + 1) / 5) / reduction_factor
        for vent_button in self.vent_buttons:
            if vent_button.is_pressed():
                self.pressure -= (4) / reduction_factor
        self.pressure += (self.tempurature_display.get_temp()/500) / reduction_factor
        self.pressure -= 13 / reduction_factor #balances out tempurature effects to make them more significant

    def draw(self):
        pressure_font = pygame.font.SysFont("comicsansms", 24)
        pressure_display = pressure_font.render(str(int(self.pressure)), True, (0,0,0))
        self.screen.blit(pressure_display, (self.x, self.y))