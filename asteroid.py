import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        split_velocity_1 = self.velocity.rotate(angle)
        split_velocity_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_1.velocity = split_velocity_1 * 1.2
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2.velocity = split_velocity_2 * 1.2