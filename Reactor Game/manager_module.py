#READ ME*******************************************************************
#READ ME*******************************************************************
#READ ME*******************************************************************
#READ ME*******************************************************************

# All comments on the right side show what numbers can be adjusted for balancing
# The reduction factor is used for balancing everything to line up with the 7k-27k goal
# Everything else adjusts how much a factor affects the variables change

import backgrounds_module
import music_module

class Manager():

    def __init__(self, screen, start_temp, start_pressure, heat_levers, cool_levers, vent_buttons, display_objects, main_buttons):
        self.screen = screen
        self.temp = start_temp
        self.pressure = start_pressure
        self.heat_levers = heat_levers
        self.cool_levers = cool_levers
        self.vent_buttons = vent_buttons
        self.display_objects = display_objects
        self.main_buttons = main_buttons
        self.power = 0
        self.reduction_factor = 33                  # higher number = slower changes
        self.timer = 500 * 60                       # 500 seconds timer
        self.background = backgrounds_module.Backgrounds(self.screen)
        self.music = music_module.Music()
        self.l_size = 0
        self.c_size = 0
        self.active_filter = "none"
        self.calculate_temp()
        self.calculate_pressure()
        self.calculate_power()
        self.music.set_music("non-operational")

    def calculate_values(self):
        self.active_filter = "none"

        if self.temp > 17000:
            # HIGH TEMPURATURE
            self.active_filter = ("yellow")

        if self.temp < 3000:
            # REACTION STALL
            self.background.reactor_background_B_()
            if self.l_size > 0:
                self.background.lasers_setup_(self.l_size)
                self.l_size -= 0.3
            self.background.lasers_()
            self.background.laser_bases_()
            if self.c_size > 0:
                self.background.core_setup_(self.c_size)
                self.c_size -= 1.5
            self.background.core_()
            self.background.reactor_background_F_()

        elif self.main_buttons[1].is_pressed():
            # INTENTIONAL SHUTDOWN
            if self.temp > 27000 or self.power < 3000:
                self.main_buttons[1].set_pressed(False)
            else:
                self.background.reactor_background_B_()
                if self.l_size > 0:
                    self.background.lasers_setup_(self.l_size)
                    self.l_size -= 0.1
                self.background.lasers_()
                self.background.laser_bases_()
                if self.c_size > 0:
                    self.background.core_setup_(self.c_size)
                    self.c_size -= 0.5
                self.background.core_()
                self.background.reactor_background_F_()

        elif self.main_buttons[0].is_pressed():
            # REGULAR OPERATIONS
            self.advance_timer()
            self.background.reactor_background_B_()
            if self.l_size < 20:
                self.background.lasers_setup_(self.l_size)
                self.l_size += 0.3
            self.background.lasers_()
            self.background.laser_bases_()
            if self.c_size < 96:
                self.background.core_setup_(self.c_size)
                self.c_size += 1.5
            self.background.core_()
            self.background.reactor_background_F_()
            self.calculate_temp()
            self.calculate_pressure()
            self.calculate_power()

        else:
            # PRE-START INACTIVE
            self.background.reactor_background_B_()
            self.background.laser_bases_()
            self.background.reactor_background_F_()


    def apply_filters(self):
        if self.active_filter == "yellow":
            self.background.yellow_filter_()
        if self.active_filter == "red":
            pass
        if self.active_filter == "none":
            pass
        

    def calculate_temp(self):
        self.change_in_temp = 0

        for heat_lever in self.heat_levers:
            self.change_in_temp += heat_lever.get_position() + 1

        for cool_lever in self.cool_levers:
            self.change_in_temp -= cool_lever.get_position() *2

        self.change_in_temp += self.pressure / 1000                  # adds more tempurature based on pressure

        self.temp += self.change_in_temp / self.reduction_factor

    def calculate_pressure(self):
        self.change_in_pressure = 0

        for heat_lever in self.heat_levers:
            self.change_in_pressure += (heat_lever.get_position() + 1) / 5   # each heat level creates 1/5 of a pressure (a maxxed lever makes 1 pressure)
                                 
        for vent_button in self.vent_buttons:                           
            if vent_button.is_pressed():
                self.change_in_pressure -= 2                                 # each vent creates -2 pressure

        self.pressure += self.change_in_pressure / self.reduction_factor

    def calculate_power(self):
        self.change_in_power = 0
        self.change_in_power += self.temp / 1000

        self.power += self.change_in_power / self.reduction_factor

    def advance_timer(self):
        self.timer -= 1

    def update_displays(self):
        self.display_objects[0].set_value(self.power)
        self.display_objects[1].set_value(self.change_in_power * 60 / self.reduction_factor)
        self.display_objects[2].set_value(self.temp)
        self.display_objects[3].set_value(self.change_in_temp * 60 / self.reduction_factor)
        self.display_objects[4].set_value(self.pressure)
        self.display_objects[5].set_value(self.change_in_pressure * 60 / self.reduction_factor)
        self.display_objects[6].set_value(self.timer / 60)
        

        for display in self.display_objects:
            display.draw()

    
    # functions below here are used for temporary testing purposes:

    def set_temp(self, num):
        self.temp = num
    
    def set_pressure(self, num):
        self.pressure = num

    def set_power(self, num):
        self.power = num


