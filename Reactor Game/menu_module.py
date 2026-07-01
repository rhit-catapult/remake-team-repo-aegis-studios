import backgrounds_module

class Menu():

    def __init__(self, screen, buttons):
        self.buttons = buttons
        self.background = backgrounds_module.Backgrounds(screen)

    def check_buttons(self):
        button_num = 0
        for button in self.buttons:
            button_num += 1
            if button.is_pressed():
                return button_num
        return -1
            
    def draw_backround(self):
        self.background.menu_()
    
        