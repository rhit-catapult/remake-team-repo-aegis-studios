import pygame

class Music():

    def __init__(self):
        
        self.active_music = "none"

    def set_music(self, new_music):
        if new_music != self.active_music:
            if new_music == "non-operational":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/non-operational1.mp3")
                self.active_music = "non-operational"
                pygame.mixer.music.play(-1)
            if new_music == "startup":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/startup1.mp3")
                self.active_music = "startup"
                pygame.mixer.music.play(-1) 
            if new_music == "hightemperature":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/hightemperature1.mp3")
                self.active_music = "hightemperature"
                pygame.mixer.music.play(-1)
            if new_music == "meltdown":
                pygame.mixer.music.load("sound/meltdown1.mp3")
                self.active_music = "meltdown"
                pygame.mixer.music.play(-1)
            if new_music == "operational":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/operational1.mp3")
                self.active_music = "operational"
                pygame.mixer.music.play(-1)
            if new_music == "reactionstall":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/reactionstall1.mp3")
                self.active_music = "reactionstall"
                pygame.mixer.music.play(-1)
            if new_music == "emergencyshutdown":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/emergencyshutdown1.mp3")
                self.active_music = "emergencyshutdown"
                pygame.mixer.music.play(-1)
            if new_music == "detonation":
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load("sound/detonation1.mp3")
                self.active_music = "detonation"
                pygame.mixer.music.play(-1)
            if new_music == "shutdown":
                pygame.mixer.music.load("sound/shutdown1.mp3")
                self.active_music = "shutdown"
                pygame.mixer.music.play(-1)
                
                