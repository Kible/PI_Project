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
exp_min = 300
exp_med = 450
spawn_cooldown = 0
last_spawn=0

#via speed
via1Speed = 0
via2Speed = 0
via3Speed = 0

def calculateStage(score):
    global via1Speed
    global via2Speed
    global via3Speed

    global exp_min
    global exp_med

    speedInc = score/3
    via1Speed = uniformeCont(3+speedInc, 3.2+speedInc)
    via2Speed = uniformeCont(3.2+speedInc, 3.4+speedInc)
    via3Speed = uniformeCont(3.6+speedInc, 3.8+speedInc)

    spawnInc = score*12
    exp_min = 300 - spawnInc
    exp_med = 450 - spawnInc

calculateStage(rabbit.score)

def spawn():
    global last_spawn
    global spawn_cooldown

    #spawn cooldown check
    if pygame.time.get_ticks()-last_spawn>=spawn_cooldown:
        last_spawn = pygame.time.get_ticks()
        spawn_cooldown = expo(exp_min, exp_med)

        #lane check
        via = uniformeDisc(0, 5)

        #car check
        car_type = binomial(2, 0.4)
        
        if via<=2:
            vehicle = sprites[car_type]
            if via==0:
                car_speed = via1Speed
            elif via==1:
                car_speed = via2Speed
            else:
                car_speed = via3Speed
            car = Vehicle.Vehicle([width,via*80+50], vehicle, car_speed*-1)
        else:
            vehicle = sprites[car_type+3]
            if via==3:
                car_speed = via3Speed
            elif via==4:
                car_speed = via2Speed
            else:
                car_speed = via1Speed
            car = Vehicle.Vehicle([0-vehicle.get_width(),via*80+90], vehicle, car_speed)

        #check for overlap on spawn
        hit = pygame.sprite.spritecollideany(car, vehicle_sprites, False)
        if not hit:
            vehicle_sprites.add(car)
        else:
            car.kill()
            del car

font = pygame.font.Font('freesansbold.ttf', 30)         
text = font.render(str(rabbit.score), True, (0,0,128))
textRect = text.get_rect()
textRect.center = (width-40, height-18)

def resetGame(score):
    global text
    
    for v in vehicle_sprites.sprites():
            v.kill()
            del v
    rabbit.reset()
    calculateStage(score)
    text = font.render(str(rabbit.score), True, (0,0,128))

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
                if rabbit.win:
                    rabbit.playWinSound()
                    resetGame(rabbit.score)
                    
    #Collision checking between vehicleGroup and Rabbit
    hit = pygame.sprite.spritecollide(rabbit, vehicle_sprites, True)
    
    if hit:
        if rabbit.score>0:
            rabbit.score = rabbit.score-1
        rabbit.playLoseSound()
        resetGame(rabbit.score)

    #Vehicle Spawner    
    spawn()
    
    #Background              
    screen.blit(background_sprite, background_sprite.get_rect())

    #Vehicle Objects Handling
    vehicle_sprites.update()
    vehicle_sprites.draw(screen)
    
    #Player Rabbit
    player_sprites.draw(screen)

    #Score
    screen.blit(text, textRect)
    
    pygame.display.flip()
    clock.tick(60)



