import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
