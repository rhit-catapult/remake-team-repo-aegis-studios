import pygame
import sys
import button_module
import lever_module
import text_display_module
import manager_module
import backgrounds_module

def main():
    pygame.init()
    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()


    heat_steps_list = [635, 620, 605, 590, 575]
    cool_steps_list = [650, 635, 620, 605, 590, 575]
    heat_list = []
    cool_list = []
    vent_list = []

    inputs = []

    for heat_lever in range(6):
        heat_list.append(lever_module.Lever(screen, 30 + 50*heat_lever, "heat_lever.png", heat_steps_list, 0))
    for cool_lever in range(3):
        cool_list.append(lever_module.Lever(screen, 900 + 50*cool_lever, "cool_lever.png", cool_steps_list, 0))
    for vent in range(3):
        vent_list.append(button_module.Button(screen, 515 + 90*vent, 605, "unpressed_button.png", "pressed_button.png", True))
    toggle_on = (button_module.Button(screen, 1150, 585, "unpressed_button.png", "pressed_button.png"))
    inputs.append(toggle_on)


    
    for lever in heat_list:
        inputs.append(lever)
    for lever in cool_list:
        inputs.append(lever)
    for button in vent_list:
        inputs.append(button)

    display_list = [
        text_display_module.Text_Display(screen, 100, 50, "Power Generated: ", "power_round"),
        text_display_module.Text_Display(screen, 100, 100, "Power Change Rate: ", "power_round"), 
        text_display_module.Text_Display(screen, 500, 50, "Tempurature: "),
        text_display_module.Text_Display(screen, 500, 100, "Temp Change Rate: ", "round"),
        text_display_module.Text_Display(screen, 900, 50, "Pressure: "),  
        text_display_module.Text_Display(screen, 900, 100, "Pressure Change Rate: ", "round"),
        text_display_module.Text_Display(screen, 1050, 650, "Time Left: ")    
    ]


    manager = manager_module.Manager(screen, 7000, 4000, heat_list, cool_list, vent_list, display_list, toggle_on)    #first 2 arguments are starting temp & pressure

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_tuple = pygame.mouse.get_pos()
                for _input in inputs:
                    if _input.is_clicked(mouse_pos_tuple[0], mouse_pos_tuple[1]):
                        _input.on_click()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos_tuple = pygame.mouse.get_pos()
                for _input in inputs:
                    _input.on_release()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    manager.set_temp(int(input("Set Temp: ")))
                if event.key == pygame.K_p:
                    manager.set_pressure(int(input("Set Pressure: ")))

        manager.calculate_values()
        manager.update_displays()


        for _input in inputs:
            if isinstance(_input, lever_module.Lever) and _input.is_held():
                _input.set_height(pygame.mouse.get_pos()[1])
            _input.draw()

       

        pygame.display.update()


main()