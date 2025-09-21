import pygame
from constants import ASTEROID_MAX_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    new_obj = pygame.time.Clock()
    player_obj = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player_obj.draw(screen)
        player_obj.update(dt)
        pygame.display.flip()
        
        new_dt = new_obj.tick(60)
        dt = new_dt / 1000

if __name__ == "__main__":
    main()
