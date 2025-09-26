import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        spawn_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_obj1 = Asteroid(self.position.x, self.position.y, spawn_asteroid_radius)
        new_obj2 = Asteroid(self.position.x, self.position.y, spawn_asteroid_radius)
        new_obj1.velocity = vel1 * 1.2
        new_obj2.velocity = vel2 * 1.2


