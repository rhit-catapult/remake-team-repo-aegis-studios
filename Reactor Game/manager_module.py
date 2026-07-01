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
        self.reduction_factor = 7                  # higher number = slower changes
        self.timer = 500 * 60                       # 500 seconds timer
        self.background = backgrounds_module.Backgrounds(self.screen)
        self.music = music_module.Music()
        self.l_size = 0
        self.c_size = 0
        self.active_filter = "none"
        self.warning = ""
        self.meltdownOn = False
        self.meltdown_timer = -1
        self.detonationOn = False
        self.detonation_timer = -1
        self.game_over = False
        self.victory = False
        self.shutdown_timer = 180
        self.calculate_temp()
        self.calculate_pressure()
        self.calculate_power()
        self.music.set_music("non-operational")
        

    def calculate_values(self):
        self.calculate_temp()
        self.calculate_pressure()
        self.calculate_power()

    def check_events(self):
        self.active_filter = "none"

        if self.game_over:
            if self.shutdown_timer > -255:
                self.shutdown_timer -= 1
            if self.shutdown_timer < 0:
                self.active_filter = "game_over"
                return
        
        if self.timer == 29999:
            # STARTUP
            self.music.set_music("startup")

        if self.timer <= 0:
            if not self.detonationOn:
                if self.power > 3000:
                    self.victory = True

        if 3000 <= self.temp < 16999 and self.timer < 27000:
            # OPERATIONAL MUSIC
            self.music.set_music("operational")
            self.warning = ""

        if 17000 <= self.temp < 26999:
            # HIGH TEMPERATURE
            self.active_filter = ("yellow")
            self.music.set_music("hightemperature")
            self.warning = "WARNING - TEMPERATURE HIGH"

        if self.temp >= 27000:
            self.active_filter = ("orange")
            self.warning = "ALERT - MELTDOWN IN PROGRESS"

        
        

        if self.main_buttons[0].is_pressed():  

            if self.main_buttons[1].is_pressed():
                if (self.power < 3000 and self.temp > 3000) or self.meltdownOn or self.detonationOn:
                    self.main_buttons[1].set_pressed(False)
                else:
                    self.e_shutoff() 
                    self.music.set_music("shutdown")             

            elif self.temp < 1000:
                self.e_shutoff()

            elif 2000 < self.temp < 3000:
                self.e_stall()
            
            elif self.temp > 27000:
                if not self.meltdownOn and not self.detonationOn:
                    self.e_start_meltdown()

                if self.meltdown_timer == 0:
                    self.e_start_detonation()

                if self.meltdownOn:
                    self.e_meltdown()

                if self.detonationOn:
                    self.meltdownOn = False
                    self.e_detonation()
         
                if 27000 < self.temp < 27005 and self.meltdown_timer < 3500:
                    self.e_shutoff() 
                    self.main_buttons[1].set_pressed(True)
                    self.music.set_music("emergencyshutdown")

            else:
                self.e_regular_operations()

        else:
            # PRE-START INACTIVE
            self.e_inactive()



    def e_inactive(self):
        print("e_inactive")
        self.background.reactor_background_B_()
        self.background.laser_bases_()
        self.background.reactor_background_F_()

    def e_regular_operations(self):
        print("e_regular_operations")
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
        self.calculate_values()
    
    def e_shutoff(self):
        # INTENTIONAL SHUTDOWN
        print("e_shutoff")
        self.temp = 0
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
        if self.power > 3000:
            self.victory = True
        self.game_over = True

    def e_stall(self):
        print("e_stall")
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
        self.music.set_music("reactionstall")
        self.game_over = True

    def e_start_meltdown(self):
        print("e_start_meltdown")
        self.meltdownOn = True
        self.meltdown_timer = 3600

    def e_meltdown(self):
        print("e_meltdown")
        self.advance_timer()
        self.background.reactor_background_B_()
        if self.l_size < 20:
            self.background.lasers_setup_(self.l_size)
            self.l_size += 0.3
        self.background.lasers_()
        self.background.laser_bases_()
        if self.c_size < 192:
            self.background.core_setup_(self.c_size)
            self.c_size += 1.5
        self.background.core_()
        self.background.reactor_background_F_()
        self.calculate_values()
        self.music.set_music("meltdown")

    def e_start_detonation(self):
        print("e_start_detonation")
        self.detonationOn = True
        self.detonation_timer = 600

    def e_detonation(self):
        print("e_detonation")
        self.active_filter = ("red")
        self.temp = 99999
        self.pressure += 10000
        self.warning = "CONTAINMENT FAILING - CRITICAL COLLAPSE IMMINENT"
        self.background.reactor_background_B_()
        if self.l_size < 30:
            self.background.lasers_setup_(self.l_size)
            self.l_size += 0.1
        self.background.lasers_()
        self.background.laser_bases_()
        if self.detonation_timer < 60:
            self.background.core_setup_(self.c_size)
            self.c_size += 15
        elif self.c_size > 43:
            self.background.core_setup_(self.c_size)
            self.c_size -= 0.4
        self.background.core_()
        self.background.reactor_background_F_()
        self.advance_timer()
        self.calculate_values() 
        self.music.set_music("detonation")
        if self.detonation_timer == 120:
            self.game_over = True


        




    def apply_filters(self):
        if self.active_filter == "yellow":
            self.background.yellow_filter_()
        if self.active_filter == "orange":
            self.background.orange_filter_()
        if self.active_filter == "red":
            self.background.red_filter_()
        if self.active_filter == "game_over":
            self.background.game_over_(self.shutdown_timer * -1, self.power, self.timer / 60, self.victory)
        

    def calculate_temp(self):
        self.change_in_temp = 0

        for heat_lever in self.heat_levers:
            self.change_in_temp += heat_lever.get_position() + 1

        for cool_lever in self.cool_levers:
            self.change_in_temp -= cool_lever.get_position() * 2

        self.change_in_temp += (self.pressure-3000) / 200                  # adds more tempurature based on pressure

        if self.meltdownOn:
            self.change_in_temp += (self.meltdown_timer + 2000) / 200   # creates a slope to stop early meltdown escapes and make later ones possible

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
        if self.meltdownOn:
            self.meltdown_timer -= 1
        if self.detonationOn:
            self.detonation_timer -= 1
        for lever in self.cool_levers + self.heat_levers:
            lever.tick_health()

    def update_displays(self):
        self.display_objects[0].set_value(self.power)
        self.display_objects[1].set_value(self.change_in_power * 60 / self.reduction_factor)
        self.display_objects[2].set_value(self.temp)
        self.display_objects[3].set_value(self.change_in_temp * 60 / self.reduction_factor)
        self.display_objects[4].set_value(self.pressure)
        self.display_objects[5].set_value(self.change_in_pressure * 60 / self.reduction_factor)
        self.display_objects[6].set_value(self.timer / 60)
        self.display_objects[7].set_value(self.warning)
        self.display_objects[8].set_value("REMAINING TIME UNTIL FULL MELTDOWN: " + str(int(self.meltdown_timer / 60)) + " s", self.meltdownOn)
        self.display_objects[9].set_value("REMAINING TIME UNTIL CRITICAL COLLAPSE: " + str(int(self.detonation_timer / 60)) + " s", self.detonationOn)
        display_string = ""
        lever_position = 0
        for lever in self.cool_levers:
            lever_position += 1
            display_string += "  COOL" + str(lever_position) + ": "
            display_string += str(int(lever.get_health()))
        self.display_objects[10].set_value("COOLANT INTEGRITY:" + display_string)
        display_string = ""
        lever_position = 0
        for lever in self.heat_levers[:3]:
            lever_position += 1
            display_string += "  CBL" + str(lever_position) + ": "
            display_string += str(int(lever.get_health()))
        self.display_objects[11].set_value("LASER INTEGRITY:" + display_string)  
        display_string = ""
        lever_position = 3
        for lever in self.heat_levers[3:]:
            lever_position += 1
            display_string += "  CBL" + str(lever_position) + ": "
            display_string += str(int(lever.get_health()))
        self.display_objects[12].set_value("                             " + display_string)  

        for display in self.display_objects:
            display.draw()

    
    # functions below here are used for temporary testing purposes:

    def set_temp(self, num):
        self.temp = num
    
    def set_pressure(self, num):
        self.pressure = num

    def set_power(self, num):
        self.power = num


