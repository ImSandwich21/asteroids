import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __ini__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle  = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = self.velocity.rotate(-random_angle) * 1.2