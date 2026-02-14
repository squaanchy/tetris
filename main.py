import random
import pygame
import grid
from block import Block
from colors import colors
from shapes import shapes
from shape_rotations import ssp


pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")
clock = pygame.Clock()
running = True
spawn_position = (4, -4)
size = 40
shape = random.choice(list(shapes.keys()))
active_block = Block(shapes[shape], random.choice(colors), size, spawn_position, ssp, shape)
grid = grid.Grid(size, "white", spawn_position, active_block)

fall_timer = 0
while running:
    screen.fill((30, 30, 30))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    grid.draw(screen)
    active_block.draw(screen, grid.cells)
    fall_timer += 1
    time = grid.fast_fall(250)
    if fall_timer >= time:
        if keys[pygame.K_SPACE]:
            grid.fast_place(active_block)
        active_block.move(grid.grid)
        active_block.falling(grid.grid, grid)
        grid.clear_line(active_block)
        if keys[pygame.K_r]:
            active_block.rotate(grid.grid)
        fall_timer = 0
    if active_block.landed:
        shape = random.choice(list(shapes.keys()))
        active_block = Block(shapes[shape], random.choice(colors), grid.size, spawn_position, ssp, shape)
    grid.draw(screen)
    pygame.display.flip()
pygame.quit()
