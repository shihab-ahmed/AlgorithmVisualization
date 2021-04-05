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
VELOCITY = 2

BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

SPACESHIP_IMG1 = pygame.image.load("rocket1.png")
SPACESHIP_IMG2 = pygame.image.load("rocket2.png")

SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG1, (64, 64)), -45)
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMG2, (64, 64)), 135)

pygame.display.set_caption("Race")


def Rocket1Controller(keys_pressed, rocketRect1):
    # Left
    if keys_pressed[pygame.K_a] and rocketRect1.x-1>0:
        rocketRect1.x -= 1
    # Right
    if keys_pressed[pygame.K_d] and rocketRect1.x+1<BORDER.x:
        rocketRect1.x += 1
    # Up
    if keys_pressed[pygame.K_w] and rocketRect1.y-1>0:
        rocketRect1.y -= 1
    # Down
    if keys_pressed[pygame.K_s] and rocketRect1.y+1<HEIGHT:
        rocketRect1.y += 1


def Rocket2Controller(keys_pressed, rocketRect2):
    # Left
    if keys_pressed[pygame.K_j]:
        rocketRect2.x -= 1
    # Right
    if keys_pressed[pygame.K_l]:
        rocketRect2.x += 1
    # Up
    if keys_pressed[pygame.K_i]:
        rocketRect2.y -= 1
    # Down
    if keys_pressed[pygame.K_k]:
        rocketRect2.y += 1


def draw_window(rocketRect1, rocketRect2):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK, BORDER)
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
        Rocket1Controller(keys_pressed, rocketRect1)
        Rocket2Controller(keys_pressed, rocketRect2)
        draw_window(rocketRect1, rocketRect2)
    pygame.quit()


if __name__ == "__main__":
    main()
