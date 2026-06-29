import pygame

class Button():
    
    def __init__(self, screen, x, y, unpressed_image_file, pressed_image_file, toggle=False):
        self.screen = screen
        self.x = x
        self.y = y
        self.unpressed_image = pygame.image.load(unpressed_image_file)
        self.pressed_image = pygame.image.load(pressed_image_file)
        self.toggle = toggle
        self.pressed = False

    def is_pressed(self):
        return self.pressed

    def on_click(self):
        if self.toggle:
            self.pressed = not self.pressed
        else:
            self.pressed = True
            
    def is_clicked(self, click_x, click_y):
        hitbox = pygame.Rect(self.x, self.y, self.unpressed_image.get_width(), self.unpressed_image.get_height())
        return hitbox.collidepoint(click_x, click_y)

    def draw(self):
        if self.pressed:
            self.screen.blit(self.pressed_image, (self.x, self.y))
        else:
            self.screen.blit(self.unpressed_image, (self.x, self.y))

