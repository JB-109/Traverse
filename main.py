import sys
import pygame
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    internal_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroid_field = AsteroidField()
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = internal_clock.tick(60) / 1000 #update the object by the time elapsed since the last tick 
        screen.fill("black")

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.is_collided(player_obj):
                print("Game Over")
                sys.exit()
        
        print(internal_clock.get_fps())
        pygame.display.flip()

if __name__ == "__main__":
    main()
