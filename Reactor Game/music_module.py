import pygame

class Music():

    def __init__(self):
        
        self.active_music = "none"

    def set_music(self, new_music):
        if new_music != self.active_music:
            if new_music == "non-operational":
                pygame.mixer.music.load("non-operational1.mp3")
            if new_music == "startup":
                pygame.mixer.music.load("startup1.mp3")
            if new_music == "operational":
                pygame.mixer.music.load("operational1.mp3")
            pygame.mixer.music.play(-1)
