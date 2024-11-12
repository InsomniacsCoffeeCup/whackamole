# This is the revised version of the whackamole file for Lab 10. It is meant to simulate a whackamole game, where
# each time the mole is "whacked", or clicked, it moves across the board. 
# November 12, 2024
# Ro Diaz

import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        row, col = 0, 0
        # inserted function for drawing the grid
        def draw_grid():
            # horizontal // vertical area is 16 boxes, so 16 horizontal lines
            for i in range(16):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (0, i * 32), (640, i * 32)
                )
            # vertical // horizontal area is 20 boxes, so 20 vertical lines
            for i in range(20):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (i * 32, 0), (i * 32, 512)
                )

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if clicked, mole moves to a random square
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rect = mole_image.get_rect(topleft = (row * 32 + 4, col * 32 + 2))
                    if mole_rect.collidepoint(event.pos):
                        # generate new random location via random number
                        row = random.randrange(0, 20)
                        col = random.randrange(0, 16)

            # When the game is running, create the screen, draw the grid, and load the mole in the top left corner
            screen.fill("light green")
            draw_grid()

            # From trial and error, the mole will appear centred in a square on the grid at the approximate location of
            # (4, 2) <-- within each individual square, not counting "total" coordinate value
            screen.blit(mole_image, mole_image.get_rect(topleft = (row * 32 + 4, col * 32 + 2)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
