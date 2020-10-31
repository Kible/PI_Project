import sys, pygame
import Rabbit, Vehicle
from Distribuicoes import *
from numpy import random

pygame.init()

#Window Size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

#Title
pygame.display.set_caption("Rabitter")

#Clock and timer
clock = pygame.time.Clock()

#Load Images
rabbit_filename = "./imgs/rabbit.png"
rabbit_sprite = pygame.image.load(rabbit_filename).convert_alpha()
background_filename = "./imgs/background.png"
background_sprite = pygame.image.load(background_filename).convert()
bikeLeft_filename = "./imgs/bikeLeft.png"
bikeLeft_sprite = pygame.image.load(bikeLeft_filename).convert_alpha()
bikeRight_filename = "./imgs/bikeRight.png"
bikeRight_sprite = pygame.image.load(bikeRight_filename).convert_alpha()
truckRight_filename = "./imgs/truckRight.png"
truckRight_sprite = pygame.image.load(truckRight_filename).convert_alpha()



#Create Player Rabbit
rabbit = Rabbit.Rabbit([width/2 - 40, height-40], rabbit_sprite)
bike = Vehicle.Vehicle([width,40], bikeLeft_sprite, -4)
bike2 = Vehicle.Vehicle([0, 44], bikeRight_sprite, 4)
truck = Vehicle.Vehicle([0, 44], truckRight_sprite, 0.7)

#Sprite Groups
player_sprites = pygame.sprite.Group(rabbit)
vehicle_sprites = pygame.sprite.Group(truck)


#Spawn cooldown/logic
exp_min = 250
exp_med = 400

spawn_cooldown = 1000
last_spawn=0

lane_numbers = 5
lane_probability = 0.5


def spawn():
    global last_spawn
    global spawn_cooldown

    global exp_min
    global exp_med

    global lane_numbers
    global lane_probability
    
    #spawn cooldown check
    if pygame.time.get_ticks()-last_spawn>=spawn_cooldown:
        last_spawn = pygame.time.get_ticks()
        spawn_cooldown = expo(exp_min, exp_med)


        #lane check
        via = binomial(lane_numbers, lane_probability)
        if via<=2:
            bike = Vehicle.Vehicle([width,via*80+44], bikeLeft_sprite, -4)
        else:
            bike = Vehicle.Vehicle([width,via*80+88], bikeLeft_sprite, -4)
        vehicle_sprites.add(bike)
        print(via)


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rabbit.move()

    #Collision checking between vehicleGroup and Rabbit
    hit = pygame.sprite.spritecollide(rabbit, vehicle_sprites, True)
    if hit:
        rabbit.reset([width/2 - 40, height-40])
        
    spawn()
    
    #Background              
    screen.blit(background_sprite, background_sprite.get_rect())

    #Vehicle Objects Handling
    vehicle_sprites.update()
    vehicle_sprites.draw(screen)
    
    #Player Rabbit
    player_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)



