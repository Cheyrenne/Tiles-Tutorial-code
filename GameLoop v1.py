import pygame
pygame.init()

# constants
WIDTH = 1920
HEIGHT =  1080

# initialize the game screen
screen = pygame.display.set_mode([WIDTH,HEIGHT],pygame.FULLSCREEN)


sprite_list = pygame.sprite.Group()

# Create platforms




done = False
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True


    #Draw platforms to screen

    clock.tick(30)
    pygame.display.flip()

pygame.quit()
