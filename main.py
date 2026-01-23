import pygame
import grid
from shapes import shapes
from block import Block


pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")
clock = pygame.Clock()
running = True
grid = grid.Grid(40, "white", 4)
dt = clock.tick(6) / 1000
fall_timer = 0
O = Block(shapes["J"], "red", grid.size, (4, 4))


while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    grid.draw(screen)
    O.draw(screen, grid.cells, grid.grid)
    grid.draw(screen)
    fall_timer += 1
    grid.grid[12][4] = 1
    time = grid.fast_fall(100)
    if fall_timer >= time:
        O.move(grid.grid)
        O.falling(grid.grid)
        fall_timer = 0
    pygame.display.flip()

pygame.quit()
