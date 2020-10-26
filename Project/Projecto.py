import sys, pygame
import Rabbit, Vehicle

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
bike2 = Vehicle.Vehicle([0, 0], bikeRight_sprite, 4)
truck = Vehicle.Vehicle([0, 44], truckRight_sprite, 0.7)

player_sprites = pygame.sprite.Group(rabbit)
vehicle_sprites = pygame.sprite.Group(truck)

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
        
        
    #Background              
    screen.blit(background_sprite, background_sprite.get_rect())

    #Vehicle Objects Handling
    vehicle_sprites.update()
    vehicle_sprites.draw(screen)
    
    #Player Rabbit
    player_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
