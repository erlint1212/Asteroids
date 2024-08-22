from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        dir1 = self.velocity.rotate(random_angle)
        dir2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS 
        astr1 = Asteroid(self.position[0], self.position[1], new_radius)
        astr2 = Asteroid(self.position[0], self.position[1], new_radius)
        astr1.velocity = dir1 * ASTEROID_SPLIT_SPEEDBOOST
        astr2.velocity = dir2 * ASTEROID_SPLIT_SPEEDBOOST

        
