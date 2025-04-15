
# import the CircleShape class from circleshape to be the parent class for Player
from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

# Player class inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # override the draw method of CircleShape, so that it looks like Triangle that represents the player and not a circle
        # pygame.draw.polygon takes a screen object, a colour, a list of points, a line width
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.cooldown -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown <= 0:
            # Create the bullet at the front of the ship
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet_pos = self.position + forward * (SHOT_RADIUS + PLAYER_RADIUS) # Position at ship's front
            print(f"Ship at ({self.position.x}, {self.position.y}), bullet spawned at ({bullet_pos.x}, {bullet_pos.y})")

            bullet = Shot(bullet_pos.x, bullet_pos.y)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED
            self.cooldown = PLAYER_SHOOT_COOLDOWN
        