# yes ik its really messy and everythings hardcoded but thats fine because its just the background, no function
import pygame


class Backgrounds():

    def __init__(self, screen):
        self.screen = screen
        self.laser_base = pygame.image.load("laser_base.png")    
        self.laser_base_60 = pygame.transform.rotate(self.laser_base, 60)
        self.laser_base_120 = pygame.transform.rotate(self.laser_base, 120)
        self.laser_base_180 = pygame.transform.rotate(self.laser_base, 180)
        self.laser_base_240 = pygame.transform.rotate(self.laser_base, 240)
        self.laser_base_300 = pygame.transform.rotate(self.laser_base, 300)
        self.rect = self.laser_base.get_rect(center=(0, 360))
        self.rect_120 = self.laser_base_60.get_rect(center=(520, 152.16))
        self.rect_60 = self.laser_base_120.get_rect(center=(760, 152.16))
        self.rect_180 = self.laser_base_180.get_rect(center=(1280, 360))
        self.rect_300 = self.laser_base_240.get_rect(center=(760, 567.84))
        self.rect_240 = self.laser_base_300.get_rect(center=(520, 567.84))

        self.reactor_backgroundB = pygame.image.load("background1-1.png")
        
        self.reactor_backgroundF = pygame.image.load("background1-2.png")

        self.yellow_filter = pygame.image.load("yellow_filter.png").convert_alpha()
        
    def laser_bases_(self):
        self.screen.blit(self.laser_base, self.rect)
        self.screen.blit(self.laser_base_60, self.rect_60)
        self.screen.blit(self.laser_base_120, self.rect_120)
        self.screen.blit(self.laser_base_180, self.rect_180)
        self.screen.blit(self.laser_base_240, self.rect_240)
        self.screen.blit(self.laser_base_300, self.rect_300)

    def lasers_setup_(self, l_size):
        self.base_laser = pygame.image.load("laser.png")
        self.laser = pygame.transform.scale(self.base_laser, (230, l_size))
        self.laser_60 = pygame.transform.rotate(self.laser, 60)
        self.laser_120 = pygame.transform.rotate(self.laser, 120)
        self.laser_180 = pygame.transform.rotate(self.laser, 180)
        self.laser_240 = pygame.transform.rotate(self.laser, 240)
        self.laser_300 = pygame.transform.rotate(self.laser, 300)
        self.l_rect = self.laser.get_rect(center=(520, 360))
        self.l_rect2 = self.laser.get_rect(center=(310, 360))
        self.l_rect3 = self.laser.get_rect(center=(100, 360))
        self.l_rect_120 = self.laser_60.get_rect(center=(580, 256.08))
        self.l_rect_60 = self.laser_120.get_rect(center=(700, 256.08))
        self.l_rect_180 = self.laser_180.get_rect(center=(760, 360))
        self.l_rect2_180 = self.laser_180.get_rect(center=(950, 360))
        self.l_rect3_180 = self.laser_180.get_rect(center=(1140, 360))
        self.l_rect_300 = self.laser_240.get_rect(center=(700, 463.92))
        self.l_rect_240 = self.laser_300.get_rect(center=(580, 463.92))

    def lasers_(self):
        self.screen.blit(self.laser, self.l_rect)
        self.screen.blit(self.laser, self.l_rect2)
        self.screen.blit(self.laser, self.l_rect3)
        self.screen.blit(self.laser_60, self.l_rect_60)
        self.screen.blit(self.laser_120, self.l_rect_120)
        self.screen.blit(self.laser_180, self.l_rect_180)
        self.screen.blit(self.laser_180, self.l_rect2_180)
        self.screen.blit(self.laser_180, self.l_rect3_180)
        self.screen.blit(self.laser_240, self.l_rect_240)
        self.screen.blit(self.laser_300, self.l_rect_300)

    def reactor_background_B_(self):
        self.screen.blit(self.reactor_backgroundB, (0,0))

    def reactor_background_F_(self):
        self.screen.blit(self.reactor_backgroundF, (0,0))
    
    def yellow_filter_(self):
        self.screen.blit(self.yellow_filter, (0,0))

    def core_setup_(self, c_size):
        self.base_core = pygame.image.load("core.png")
        self.core = pygame.transform.scale(self.base_core, (c_size, c_size))
        self.core_rect = self.core.get_rect(center=(640, 360))

    def core_(self):
        self.screen.blit(self.core, self.core_rect)










