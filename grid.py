import pygame


class Grid:
    def __init__(self, size, color, buffer_size):
        self.size = size
        self.buffer_size = buffer_size
        self.grid = [[0 for i in range(10)] for x in range(20)]
        self.buffer = [[0 for i in range(buffer_size)] for v in range(buffer_size)]
        self.color = color
        self.cells = []

    def draw(self, surface):
        self.cells.clear()
        for x in range(0, surface.get_width(), self.size):
            n = []
            for y in range(0, surface.get_height(), self.size):
                d = pygame.draw.rect(surface, self.color, (x, y, self.size, self.size), width=1)
                n.append(d)
            self.cells.append(n)
        self.draw_grid(surface)

    def add_block(self):
        pass

    def draw_grid(self, surface):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    pygame.draw.rect(surface, self.color, (self.cells[j][i][0], self.cells[j][i][1], self.size, self.size), width=1)
                else:
                    pygame.draw.rect(surface, self.color, (self.cells[j][i][0], self.cells[j][i][1], self.size, self.size))

    def fast_fall(self, time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            time = 40
            return time
        time = 90
        return time