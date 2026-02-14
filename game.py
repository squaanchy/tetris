import pygame
from grid import Grid


class UI:
    def __init__(self, color, size, grid):
        self.size = size
        self.color = color
        self.grid = grid
        self.rec = None

    def draw_ui(self, surface):
        rec = pygame.draw.rect(surface, self.color, (30, 50, self.size[0], self.size[1]), width=1)
        self.rec = rec

    def draw_game_over_screen(self, surface):
        pass

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris")
clock = pygame.Clock()
running = True

size = 20
grid = Grid(size, "white", (0, 0), "")
interace = UI("white", (250, 500), grid)

while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    interace.draw_ui(screen)
    pygame.display.flip()
pygame.quit()
