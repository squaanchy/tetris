import pygame


class Block:
    def __init__(self, shape, color, size, anchor):
        self.shape = shape
        self.color = color
        self.size = size
        self.anchor = [anchor[0], anchor[1]]
        self.cubes = []

    def add_shape(self, grid):
        for anchor in self.current_cells():
            grid[anchor[1]][anchor[0]] = 1

    def current_cells(self):
        l = []
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    l.append((self.anchor[0]+j, self.anchor[1]+i))
        return l

    def can_fall(self, grid):
        for i in range(len(self.shape[-1])):
            if self.anchor[1] <= len(grid) - len(self.shape) - 1:
                return True
            if self.shape[i+1][-1] != 1:
                return True
            return False

    def is_valid(self, grid):
        pass

    def move(self, grid):
        keys = pygame.key.get_pressed()
        if self.can_fall(grid):
            if self.anchor[0] <= len(grid[0]) - len(self.shape[0]) - 1:
                if keys[pygame.K_RIGHT]:
                    self.anchor[0] += 1
            if self.anchor[0] > 0:
                if keys[pygame.K_LEFT]:
                    self.anchor[0] -= 1

    def draw(self, surface, cells, grid):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    cube = pygame.draw.rect(surface, self.color, (cells[self.anchor[0]+j][self.anchor[1]+i][0], cells[self.anchor[0]+j][self.anchor[1]+i][1], self.size, self.size))
                    self.cubes.append(cube)

    def falling(self, grid):
        if self.can_fall(grid):
            self.anchor[1] += 1
        else:
            self.add_shape(grid)



