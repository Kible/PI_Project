import pygame 

from Distribuicoes import *

class Rabbit(pygame.sprite.Sprite):
    
    def __init__(self, position, sprite):
        super().__init__()
        print("Hello im a Rabbit")
        self.image = sprite
        self.rect = sprite.get_rect()
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        #Last_Jump timer and Cooldown
        self.last_jump = 0
        self.cooldown = 1000
        
    def move(self):
        if pygame.time.get_ticks()-self.last_jump>=self.cooldown:
            #update cooldown timer
            self.last_jump = pygame.time.get_ticks()
            self.cooldown = normal(500, 200)
            print(self.cooldown)
            
            #move the rabbit
            self.position[1] = self.position[1]-40
            self.rect.y = self.position[1]
            print(self.rect)


    def reset(self, position):
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
    

    

    


        
       

    

