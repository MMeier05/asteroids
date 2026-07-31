from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x: float, y:float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        first_asteroid_vel = self.velocity.rotate(random.uniform(20, 50))
        second_asteroid_vel = self.velocity.rotate(random.uniform(20, 50))
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position[0], self.position[1], new_rad)
        new_ast2 = Asteroid(self.position[0], self.position[1], new_rad)
        new_ast1.velocity = first_asteroid_vel * 1.2
        new_ast2.velocity = second_asteroid_vel * 1.2
