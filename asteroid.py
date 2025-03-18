import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    # spliting asteroids when shot
    def split(self):
        # we kill (disappear) all asteroids
        self.kill()

        # if smallest, then that's it (we killed it), if larger, we spawn new ones 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # spawning new asteroids
        # generate random number between 20-50
        random_angle = random.uniform(20, 50)
        # generate new velocity and radius for new asteroids
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # generate new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2
