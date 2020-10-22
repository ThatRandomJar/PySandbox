import pygame
import random

WIDTH = 800
HEIGHT = 600

Spawnpos = ()

WHITE = (255, 255, 255)
RED = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (135, 206, 235)
YELLOW = (255,255,0)

draw = False

gravity = 3

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sandbox")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, color):

        self.move_y = gravity
        self.size = 4
        self.range = random.randrange(-10, 10)
        self.x = 300
        self.y = 300
        self.color = color

    def move(self):
        self.y += self.move_y 
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT -2: self.y = HEIGHT - 2


def draw_environment(dot):
    game_display.fill(CYAN)
    while True:
        if draw == True:
            pygame.draw.circle(game_display, dot.color, Spawnpos, dot.size)
            dot.move()
        print(pygame.mouse.get_pos())
    pygame.display.update()


def main():
    sand_dot = [Particle(color = YELLOW)]
    while True:
        Spawnpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:  draw = True
            else: draw = False
        draw_environment(sand_dot)
        clock.tick(20)

if __name__ == "__main__":
    main()