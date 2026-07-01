import pygame
import sys
import button_module
import lever_module
import text_display_module
import manager_module

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Starfall: Hydra - Reactor Operations")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()


    heat_steps_list = [630, 615, 600, 585, 570]
    cool_steps_list = [645, 630, 615, 600, 585, 570]
    heat_list = []
    cool_list = []
    vent_list = []
    main_button_list = []

    inputs = []

    for heat_lever in range(6):
        heat_list.append(lever_module.Lever(screen, 20 + 58*heat_lever, "image/heat_lever.png", heat_steps_list, 0))
    for cool_lever in range(3):
        cool_list.append(lever_module.Lever(screen, 1105 + 58*cool_lever, "image/cool_lever.png", cool_steps_list, 0))
    for vent in range(3):
        vent_list.append(button_module.Button(screen, 950.5 + 53*vent, 574, "image/unpressed_button.png", "image/pressed_button.png", True))
    for main_button in range(2):
        main_button_list.append(button_module.Button(screen, 594 + 62*main_button, 623, "image/unpressed_button.png", "image/pressed_button.png"))
    

    for lever in heat_list:
        inputs.append(lever)
    for lever in cool_list:
        inputs.append(lever)
    for button in vent_list:
        inputs.append(button)
    for button in main_button_list:
        inputs.append(button)

    display_list = [
        text_display_module.Text_Display(screen, 485, 40, "Power Generated: ", "power_round"),
        text_display_module.Text_Display(screen, 485, 60, "Power Generation Rate: ", "power_round"), 
        text_display_module.Text_Display(screen, 485, 80, "Temperature: ", "temp"),
        text_display_module.Text_Display(screen, 485, 100, "Temp Change Rate: ", "temp_round"),
        text_display_module.Text_Display(screen, 835, 20, "Pressure: ", "pressure"),
        text_display_module.Text_Display(screen, 835, 40, "Pressure Change Rate: ", "pressure_round"),
        text_display_module.Text_Display(screen, 485, 20, "Remaining Shift Time: ", "time_left"),
        text_display_module.Text_Display(screen, 25, 20, ""), 
        text_display_module.Text_Display(screen, 25, 40, ""), 
        text_display_module.Text_Display(screen, 25, 40, "") 
    ]


    manager = manager_module.Manager(screen, 7000, 4000, heat_list, cool_list, vent_list, display_list, main_button_list)    #first 2 arguments are starting temp & pressure

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
                if event.key == pygame.K_o:
                    manager.set_power(int(input("Set Power: ")))

        manager.check_events()
        manager.update_displays()


        for _input in inputs:
            if isinstance(_input, lever_module.Lever) and _input.is_held():
                _input.set_height(pygame.mouse.get_pos()[1])
            _input.draw()

        manager.apply_filters()
        print("---")

        pygame.display.update()


main()