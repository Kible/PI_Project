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

#Load Rabbit+Background
rabbit_filename = "./imgs/rabbit.png"
rabbit_sprite = pygame.image.load(rabbit_filename).convert_alpha()
background_filename = "./imgs/background.png"
background_sprite = pygame.image.load(background_filename).convert()

#Load Vehicles
bikeLeft_filename = "./imgs/bikeLeft.png"
bikeRight_filename = "./imgs/bikeRight.png"
truckLeft_filename = "./imgs/truckLeft.png"
truckRight_filename = "./imgs/truckRight.png"
carLeft_filename = "./imgs/carLeft.png"
carRight_filename = "./imgs/carRight.png"

fileNames=[bikeLeft_filename, carLeft_filename, truckLeft_filename, bikeRight_filename, carRight_filename, truckRight_filename]
sprites = []
for i in range(6):
    sprites.append(pygame.image.load(fileNames[i]).convert_alpha())

#Create Player Rabbit
rabbit = Rabbit.Rabbit([width, height], rabbit_sprite)

#Sprite Groups
player_sprites = pygame.sprite.Group(rabbit)
vehicle_sprites = pygame.sprite.Group()


#Spawn cooldown/logic
exp_min = 250
exp_med = 450
spawn_cooldown = 500
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
        via = uniformeCont(0, 5)

        #car check
        car_type = binomial(2, 0.5)

        #vel
        car_vel = uniformeDisc(3, 3.3)
        
        if via<=2:
            vehicle = sprites[car_type]
            car = Vehicle.Vehicle([width,via*80+50], vehicle, car_vel*-1)
        else:
            vehicle = sprites[car_type+3]
            car = Vehicle.Vehicle([0-vehicle.get_width(),via*80+90], vehicle, car_vel)
        vehicle_sprites.add(car)
        


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
        rabbit.reset()
        if rabbit.score>0:
            rabbit.score = rabbit.score-1
        print(rabbit.score)
        
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



