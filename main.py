# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create the game loop
    countera = 0
    while countera < 10000:
        screen.fill(0x000000)
        countera += 1
        pygame.display.flip()


if __name__ == "__main__":
    main()
