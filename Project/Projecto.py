import sys, pygame
import Rabbit

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

#Create Player Rabbit
rabbit = Rabbit.Rabbit([0,560 ], rabbit_sprite)

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

                
    screen.blit(background_sprite, background_sprite.get_rect())
    screen.blit(rabbit_sprite, rabbit.rect)
    pygame.display.flip()
    clock.tick(60)
