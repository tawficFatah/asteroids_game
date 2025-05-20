import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20 ,50)
        
        vect_1 = self.velocity.rotate(angle)
        vect_2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vect_1
        asteroid_1.velocity *= 1.2
        
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vect_2
        asteroid_2.velocity *= 1.2