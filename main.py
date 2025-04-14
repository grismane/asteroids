# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create the game loop
    while True:
        # prevent infinite looping by making the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000000)

        player.update(dt)

        # draw the player object
        player.draw(screen)

        # update the image with the current state of the game
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
