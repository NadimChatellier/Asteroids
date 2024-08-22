# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups here
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Assign the newly created groups to Player.containers before instantiation
    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable)

    AsteroidField.containers = (updatable)

    
    
    
    # Now create the player instance
    P1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))

        # Iterate drawable and updatable groups to draw and update all sprites
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()