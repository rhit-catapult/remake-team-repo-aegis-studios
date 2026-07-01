import pygame

class Lever():
    
    def __init__(self, screen, x, handle_image_file, steps_y_list, start_pos, lever_type, visibility):
        self.screen = screen
        self.x = x
        self.y = steps_y_list[start_pos]
        self.lever_image = pygame.image.load(handle_image_file)
        self.steps_y_list =steps_y_list
        self.pos = start_pos
        self.held = False
        self.health = 100
        self.lever_type = lever_type
        self.visibility = visibility

    def get_vis(self):
        return self.visibility

    def get_position(self):
        if self.lever_type == "heat":
            return self.pos + 1
        else:
            return self.pos

    def is_clicked(self, click_x, click_y):
        hitbox = pygame.Rect(self.x, self.y, self.lever_image.get_width(), self.lever_image.get_height())
        return hitbox.collidepoint(click_x, click_y)
    
    def is_held(self):
        return self.held
    
    def set_height(self, y):
        if y < min(self.steps_y_list):
            self.y = min(self.steps_y_list)
        elif y > max(self.steps_y_list):
            self.y = max(self.steps_y_list)
        else:
            self.y = y

    def on_click(self):
        if self.health > 0:
            self.held = True

    def on_release(self):
        closest = self.steps_y_list[0]
        for snap_point in self.steps_y_list:
            if abs(self.y - snap_point) < abs(self.y - closest):
                closest = snap_point
        self.y = closest
        self.pos = self.steps_y_list.index(closest)
        self.held = False

    def draw(self):
        self.screen.blit(self.lever_image,(self.x, self.y))
        
    def tick_health(self):
        if self.health <= 0:
            self.health = 0 
        else:
            if self.lever_type == "heat":
                self.health -= (0.2) * (self.pos + 1) / 60
            else:
                self.health -= (0.2) * self.pos / 60

    def get_health(self):
        return self.health
            

    
