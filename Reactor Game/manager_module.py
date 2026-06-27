#READ ME*******************************************************************
#READ ME*******************************************************************
#READ ME*******************************************************************
#READ ME*******************************************************************

# All comments on the right side show what numbers can be adjusted for balancing
# The reduction factor is used for balancing everything to line up with the 7k-27k goal
# Everything else adjusts how much a factor affects the variables change

class Manager():

    def __init__(self, start_temp, start_pressure, heat_levers, cool_levers, vent_buttons, display_objects):
        self.temp = start_temp
        self.pressure = start_pressure
        self.heat_levers = heat_levers
        self.cool_levers = cool_levers
        self.vent_buttons = vent_buttons
        self.display_objects = display_objects
        self.power = 0
        self.reduction_factor = 33                  # higher number = slower changes
        self.timer = 500 * 60                       # 500 seconds timer  

    def calculate_values(self):
        self.calculate_temp()
        self.calculate_pressure()
        self.calculate_power()
        self.advance_timer()

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
        self.change_in_power += self.temp

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


