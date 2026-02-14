import pygame

class UI:
    def __init__(self, color, size):
        self.size = size
        self.color = color

    def draw(self, surface):
        pass

pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")
clock = pygame.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
