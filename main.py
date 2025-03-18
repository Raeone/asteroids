import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # pygame initialization
    pygame.init()
    
    # open window for a game (save as screen object)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # pygame FPS limitation
    clock = pygame.time.Clock()

    # group objects - create pygame groups (after creating class, import group of its objects here, so you can use them)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add containers attribut to Player class (to all player objects)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )    
    asteroid_field = AsteroidField()
    
    # delta time variable
    dt = 0

    # game loop (infinite loop)
    while True:
        # end loop when game window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill game window (screen) black
        screen.fill((0, 0, 0))
        
        # draw game / circleshape objects (every object in drawable group)
        for obj in drawable:
            obj.draw(screen)
        # update game / circleshape objects (every object in updatable group)
        updatable.update(dt)

        # exit game if asteroids are colliding with player
        for asteroid in asteroids:
            if asteroid.are_colliding(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots: 
                if asteroid.are_colliding(shot):
                    asteroid.kill()
                    shot.kill()
        
        # refresh screen
        pygame.display.flip() 

        # set delta time (used in movement calculations)
        dt = clock.tick(60) / 1000

# app can be start directly via main.py (main.py cannot be imported and started as a module)
if __name__ == "__main__":
    main()
