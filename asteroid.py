import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        position_tuple = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", position_tuple, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt