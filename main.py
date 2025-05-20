import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # getting a pygame time clock object
    clock = pygame.time.Clock()
    
    # all the objects that can be updated
    updatable = pygame.sprite.Group()
    # all the objects that can be drawn
    drawable = pygame.sprite.Group()
    # group for the asteroids
    asteroids = pygame.sprite.Group()
    # All the shots
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player_x = SCREEN_WIDTH  / 2
    player_y = SCREEN_HEIGHT / 2

    player = Player(player_x, player_y)
    asteroid_field = AsteroidField()

    updatable.add(player)
    drawable.add(player)


    dt = 0
    continue_running = True

    while continue_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_running = False

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()        
                    asteroid.split()
                    
        screen.fill("black")

        # drawing the player
        for object in drawable:
            object.draw(screen)
            
        #player.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS        
        dt = clock.tick() / 1000
        
if __name__ == "__main__":
    main()