import pygame
from constants import *
from player import Player

def main():
    # initialize pygame
    init_results = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # getting a pygame time clock object
    clock = pygame.time.Clock()
    
    # all the objects that can be updated
    updatable = pygame.sprite.Group()
    # all the objects that can be drawn
    drawable = pygame.sprite.Group()

    player_x = SCREEN_WIDTH  / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    Player.containers = (updatable, drawable)

    updatable.add(player)
    drawable.add(player)

    dt = 0
    continue_running = True

    while continue_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_running = False

        updatable.update(dt)
        #player.update(dt)
        
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