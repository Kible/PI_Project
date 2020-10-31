import pygame 

from Distribuicoes import *

class Rabbit(pygame.sprite.Sprite):
    
    def __init__(self, screen, sprite):
        super().__init__()
        print("Hello im a Rabbit")
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
        
    def move(self):
        if pygame.time.get_ticks()-self.last_jump>=self.cooldown:
            #update cooldown timer
            self.last_jump = pygame.time.get_ticks()
            self.cooldown = normal(500, 200)
            
            
            #move the rabbit
            self.position[1] = self.position[1]-40
            self.rect.y = self.position[1]

            if(self.position[1] == 0):
                self.score = self.score + 1
                self.reset()
                print(self.score)

    def reset(self):
        self.position = [self.screen[0]/2 - 40, self.screen[1]-40]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
    

    


        
       

    

