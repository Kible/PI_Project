import pygame
from numpy import random, sqrt, log

class Rabbit:
    
    def __init__(self, position, sprite):
        print("Hello im a Rabbit")
        self.sprite = sprite
        self.position = position
        self.rect = sprite.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        #Last_Jump timer and Cooldown
        self.last_jump = 0
        self.cooldown = 1000
        
    def move(self):
        if pygame.time.get_ticks()-self.last_jump>=self.cooldown:
            #update cooldown timer
            self.last_jump = pygame.time.get_ticks()
            self.cooldown = self.guass()
            print(self.cooldown)
            #move the rabbit
            self.position[1] = self.position[1]-40
            self.rect.y = self.position[1]
            print(self.rect)

    #chamada a funcao do numpy
    def guass(self):
        x = random.normal(loc=500, scale=200, size=1)
        return x[0]


    

#Implementacao do algoritmo
def normal(mu, sigma):
        #Unif intervalo [0, 1]
        #To sample Unif[a, b], b > a multiply the output of random_sample by (b-a) and add a:
        #[-1,1] => a=-1 && b = 1
        a=-1
        b=1
        while True:
            u1 = random.random()*(b-a)+a
            u2 = random.random()*(b-a)+a
            u = u1**2 + u2**2
            if u<1:
                break
        return mu + sigma * u1 * sqrt(-2.0 * log(u)/u)
        
       

    

