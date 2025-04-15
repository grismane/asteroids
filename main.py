# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    # CLI outputs
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame
    pygame.init()

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # initialize the game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # create object groups
    updatable = pygame.sprite.Group() # all the objects that can be updated
    drawable = pygame.sprite.Group() # all the objects that can be drawn
    asteroids = pygame.sprite.Group() # all asteroids
    shots = pygame.sprite.Group() # all shots
    Player.containers = (updatable, drawable) # set these groups as containers for the player
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # create the player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create an asteroid field object
    ast_field =  AsteroidField()

    # create the game loop
    while True:
        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000

        # prevent infinite looping by making the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update updatable objects
        updatable.update(dt)

        # check for bullet-asteroid collisions
        for ast in asteroids:
            for bullet in shots:
                if bullet.check_collision(ast):
                    bullet.kill()
                    ast.kill()

        # check for player-asteroid collisions
        for ast in asteroids:
            if player.check_collision(ast):
                print("Game over!")
                raise SystemExit

        # draw everything
        screen.fill(0x000000)
        for obj in drawable:
            obj.draw(screen)
        # update the image with the current state of the game
        pygame.display.flip()        

if __name__ == "__main__":
    main()
