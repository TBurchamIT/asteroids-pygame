import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        new_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(new_angle)
        velocity2 = self.velocity.rotate(- new_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity1 * 1.2
            new_asteroid2.velocity = velocity2 * 1.2

