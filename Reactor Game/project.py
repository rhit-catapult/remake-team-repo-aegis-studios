import pygame
import sys
import button_module
import lever_module
import tempurature_module
import pressure_module

def main():
    pygame.init()
    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()


    heat_steps_list = [500, 400, 300, 200, 100]
    cool_steps_list = [600, 500, 400, 300, 200, 100]
    heat_list = []
    cool_list = []
    vent_list = []

    inputs = []

    for heat_lever in range(6):
        heat_list.append(lever_module.Lever(screen, 400 + 100*heat_lever, "lever_placeholder.png", heat_steps_list, 0))
    for cool_lever in range(3):
        cool_list.append(lever_module.Lever(screen, 100*cool_lever, "cool_lever_placeholder.png", cool_steps_list, 0))
    for vent in range(3):
        vent_list.append(button_module.Button(screen, 500 + 110*vent, 600, "red_placeholder.png", "green_placeholder.png", True))


    
    for lever in heat_list:
        inputs.append(lever)
    for lever in cool_list:
        inputs.append(lever)
    for button in vent_list:
        inputs.append(button)

    displays = []

    tempurature_display = tempurature_module.Tempurature(screen, 800, 50, 7000, heat_list, cool_list)
    pressure_display = pressure_module.Pressure(screen, 800, 150, 4000, heat_list, vent_list, tempurature_display)

    displays.append(tempurature_display)
    displays.append(pressure_display)

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
                for _input in inputs:
                    _input.on_release()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    tempurature_display.set_temp()
                if event.key == pygame.K_p:
                    pressure_display.set_pressure()




        screen.fill((255, 255, 255))


        for _input in inputs:
            if isinstance(_input, lever_module.Lever) and _input.is_held():
                _input.set_y(pygame.mouse.get_pos()[1])
            _input.draw()

        for display in displays:
            display.update_values()
            display.draw()

        pygame.display.update()


main()