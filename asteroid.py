from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_angle = random.uniform(20, 50)
            angles = [-new_angle, new_angle]
            for angle in angles:
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(angle) * 1.2
            self.kill()