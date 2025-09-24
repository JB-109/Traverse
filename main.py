import pygame
from constants import *
from player import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    internal_clock = pygame.time.Clock()
    player_obj = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = internal_clock.tick(60) / 1000 #update the object by the time elapsed since the last tick 

        screen.fill("black")
        player_obj.update(dt)
        player_obj.draw(screen)
        
        print(internal_clock.get_fps())

        pygame.display.flip()

if __name__ == "__main__":
    main()
