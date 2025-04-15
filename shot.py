import pygame
from circleshape import CircleShape
from constants import *

# shot class inherits from CircleShape
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        position_tuple = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", position_tuple, self.radius, 2)

    def update(self, dt):
        # Move the bullet according to its velocity
        self.position += self.velocity * dt

        # Remove bullets that go off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # Remove from all sprite groups