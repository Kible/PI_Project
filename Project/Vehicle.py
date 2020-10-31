import pygame

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, position, sprite, vel):
        super().__init__()
        self.image = sprite
        self.rect = sprite.get_rect()
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.vel = vel
        

    def update(self):
        self.position[0] = self.position[0]+self.vel
        self.rect.x = self.position[0]
        
        if not pygame.Rect(-200, 0, 1200, 600).contains(self.rect):
            self.kill()
            del self

    
