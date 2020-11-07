import pygame 
from Distribuicoes import *

#Load Rabbit Sound
pygame.mixer.init()
rabbit_jump_Sound = pygame.mixer.Sound("./sound/rabbit_jump.wav")
rabbit_win_Sound = pygame.mixer.Sound("./sound/win.wav")
rabbit_lose_Sound = pygame.mixer.Sound("./sound/lose.wav")

class Rabbit(pygame.sprite.Sprite):
    
    def __init__(self, screen, sprite):
        super().__init__()
        self.image = sprite
        self.rect = sprite.get_rect()
        self.screen = screen
        self.position = [self.screen[0]/2 - 40, self.screen[1]-40]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.score = 0
        
        #Last_Jump timer and Cooldown
        self.last_jump = 0
        self.cooldown = 1000

        self.win = False

        
    def move(self):
        if pygame.time.get_ticks()-self.last_jump>=self.cooldown:

            rabbit_jump_Sound.play()
            
            #update cooldown timer
            self.last_jump = pygame.time.get_ticks()
            self.cooldown = normal(300, 100)
            
            #move the rabbit
            self.position[1] = self.position[1]-40
            self.rect.y = self.position[1] 
            
            if(self.position[1] == 0):
                self.win = True
                self.score = self.score+1
                

    def reset(self):
        self.position = [self.screen[0]/2 - 40, self.screen[1]-40]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

        self.win = False
        

    def playWinSound(self):
        rabbit_win_Sound.play()

    def playLoseSound(self):
        rabbit_lose_Sound.play()

    

