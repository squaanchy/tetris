import random
import pygame

from block import Block
from colors import colors
from grid import Grid
from shape_rotations import ssp
from shapes import shapes

pygame.font.init()

class UI:
    def __init__(self, color, size, grid):
        self.size = size
        self.color = color
        self.grid = grid
        self.rec = None
        self.surf = None
        self.font = pygame.font.SysFont("Helvetica", 20)
        self.score = 0

    def draw_ui(self, surface, s):
        surf = pygame.Surface((self.size[0], self.size[1]))
        surf.fill((30, 30, 30))
        rec = pygame.draw.rect(surf, self.color, (0, 0, self.size[0], self.size[1]), width=1)
        rec2 = pygame.draw.rect(surface, self.color, (284, 100, 100, 200), width=1)
        self.rec = rec
        score_txt = self.font.render("Score:", True, (255, 255, 255))
        scr = self.font.render(f"{int(self.score)}", True, (255, 255, 255))
        surface.blit(score_txt, (310, 310))
        surface.blit(scr, (325, 335))
        self.surf = surf
        surface.blit(self.surf, (20, 50))

    def draw_game_over_screen(self, surface):
        pass


pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris")

clock = pygame.Clock()
running = True
spawn_position = (4, -4)
size = 23
shape = random.choice(list(shapes.keys()))
active_block = Block(shapes[shape], random.choice(colors), size, spawn_position, ssp, shape)
next_block = Block(shapes[shape], random.choice(colors), size, spawn_position, ssp, shape)
grid = Grid(size, "white", spawn_position, active_block)
interface = UI("white", (230, 460), grid)



fall_timer = 0
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    interface.draw_ui(screen, next_block)
    grid.draw(interface.surf)
    active_block.draw(interface.surf, grid.cells)
    screen.blit(interface.surf, (20, 50))
    keys = pygame.key.get_pressed()
    if grid.game_over == False:
        fall_timer += 1
        time = grid.fast_fall(250)
        if fall_timer >= time:
            if keys[pygame.K_SPACE]:
                grid.fast_place(active_block)
            active_block.move(grid.grid)
            active_block.falling(grid.grid, grid)
            grid.clear_line(active_block, active_block.anchor[1], interface)
            if keys[pygame.K_r]:
                active_block.rotate(grid.grid)
            fall_timer = 0
        if active_block.landed:
            shape = random.choice(list(shapes.keys()))
            active_block = Block(shapes[shape], random.choice(colors), grid.size, spawn_position, ssp, shape)
        grid.draw(interface.surf)
        active_block.losing(grid.grid, grid)
    pygame.display.flip()
pygame.quit()
