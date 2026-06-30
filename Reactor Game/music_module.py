import pygame

class Music():

    def __init__(self):
        
        self.active_music = "none"

    def set_music(self, new_music):
        if not pygame.mixer.music.get_busy():
            new_music = "operational"
            self.active_music = "none"
        if new_music != self.active_music:
            if new_music == "non-operational":
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.load("sound/non-operational1.mp3")
                self.active_music = "non-operational"
                pygame.mixer.music.play(-1)
            if new_music == "startup":
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.load("sound/startup1.mp3")
                self.active_music = "startup"
                pygame.mixer.music.play(0) 
            if new_music == "hightemperature":
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.load("sound/hightemperature1.mp3")
                self.active_music = "hightemperature"
                pygame.mixer.music.play(-1)
            if new_music == "operational" and self.active_music != "startup":
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.load("sound/operational1.mp3")
                self.active_music = "operational"
                pygame.mixer.music.play(-1)


