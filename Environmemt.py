import pygame
import random

WIDTH = 800
HEIGHT = 600

dotCount = 1

WHITE = (255, 255, 255)
RED = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (135, 206, 235)
YELLOW = (255,255,0)

draw = False

gravity = 5

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sandbox")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, color):
        self.move_y = gravity
        self.size = 4
        p, q = random.randint(-10, 10), random.randint(5, 5)
        self.range= (p, q)
        self.position = pygame.mouse.get_pos() + self.range
        self.color = color

    def move(self):
        self.y += self.move_y 
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT -2: self.y = HEIGHT - 2


def draw_environment(dots):
    game_display.fill(CYAN)
    for dot in dots:
        pygame.draw.circle(game_display, dot.color, dot.position, dot.size)
        dot.move()
    pygame.display.update()



def main():
    sand_dots = [Particle(color = YELLOW) for i in range(dotCount)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(sand_dots)
        clock.tick(60)

if __name__ == "__main__":
    main()