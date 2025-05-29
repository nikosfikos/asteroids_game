from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS
import asteroid


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,2)

    def update(self,dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vel1= self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)
            smaller_asteroid1 = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            smaller_asteroid2 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            smaller_asteroid1.velocity = vel1 * 1.2
            smaller_asteroid2.velocity = vel2 * 1.2
