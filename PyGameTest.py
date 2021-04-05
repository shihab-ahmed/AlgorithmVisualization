import pygame
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

SPACESHIP_IMG1 = pygame.image.load("rocket1.png")
SPACESHIP_IMG2 = pygame.image.load("rocket2.png")

SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG1, (64, 64)), -45)
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG2, (64, 64)), 135)

pygame.display.set_caption("Race")


def draw_window(rocketRect1, rocketRect2):
    WIN.fill(WHITE)
    WIN.blit(SPACESHIP1, (rocketRect1.x, rocketRect1.y))
    WIN.blit(SPACESHIP2, (rocketRect2.x, rocketRect2.y))
    pygame.display.update()


def main():
    rocketRect1 = pygame.Rect(100, 300, 64, 64)
    rocketRect2 = pygame.Rect(700, 300, 64, 64)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        #Left
        if keys_pressed[pygame.K_a]:
            rocketRect1.x -= 1
        # Right
        if keys_pressed[pygame.K_d]:
            rocketRect1.x += 1
        # Up
        if keys_pressed[pygame.K_w]:
            rocketRect1.y -= 1
        # Down
        if keys_pressed[pygame.K_s]:
            rocketRect1.y += 1
        draw_window(rocketRect1, rocketRect2)
    pygame.quit()


if __name__ == "__main__":
    main()
