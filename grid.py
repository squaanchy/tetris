import pygame


class Grid:
    def __init__(self, size, color, anchor, block):
        self.size = size
        self.grid = [[0 for i in range(10)] for x in range(20)]
        self.cells = []
        self.color = color
        self.block = block
        self.color = color
        self.cells = []
        self.anchor = anchor
        self.block = block
        self.line = []

    def draw(self, surface):
        self.cells.clear()
        for x in range(0, surface.get_width(), self.size):
            n = []
            for y in range(0, surface.get_height(), self.size):
                d = pygame.draw.rect(surface, self.color, (x, y, self.size, self.size), width=1)
                n.append(d)
            self.cells.append(n)
        self.draw_grid(surface)
    def draw_grid(self, surface):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    pygame.draw.rect(surface, self.color, (self.cells[j][i][0], self.cells[j][i][1], self.size, self.size), width=1)
                else:
                    pygame.draw.rect(surface, self.color, (self.cells[j][i][0], self.cells[j][i][1], self.size, self.size))

    @staticmethod
    def fast_fall(time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            time = time // 2
            return time
        return time

    def fall(self):
        pass

    def fast_place(self, block):
        while block.can_place(self.grid):
            block.falling(self.grid, self)

    def can_clear(self):
        for row in range(len(self.grid)):
            if all(self.grid[row]) == 1:
                return True
        return False

    def clear_line(self, row): # Use self.shape in a for loop
        for col in range(len(self.grid[-1])):
            if self.can_clear():
                self.grid.remove(self.grid[row][col])

