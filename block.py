import pygame


class Block:
    def __init__(self, shape, color, size, anchor, rotations, form):
        self.shape = shape
        self.form = form
        self.color = color
        self.size = size
        self.anchor = [anchor[0], anchor[1]]
        self.cubes = []
        self.landed = False
        self.in_buffer = False
        self.rotation = 0
        self.rotations = rotations

    def add_shape(self, grid, i, j):
        for anchor in self.current_cells():
            grid[anchor[1]+i][anchor[0]+j] = 1

    def current_cells(self):
        l = []
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    l.append((self.anchor[0]+j, self.anchor[1]+i))
        return l

    def can_fall(self, grid):
        for x, y in self.current_cells():
            if y > 0:
                if y + 1 >= len(grid):
                    return False
                if grid[y + 1][x] == 1:
                    return False

        return True

    def is_valid_right(self, grid):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.anchor[0] + j < 0 or self.anchor[0] + j >= len(grid[0]) or self.anchor[1] + i >= len(grid):
                    return False
                if self.anchor[1] + i >= 0 and grid[self.anchor[1] + i][self.anchor[0] + j + 1] == 1:
                    return False
        return True

    def is_valid_left(self, grid):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.anchor[0] + j < 0 or self.anchor[0] + j >= len(grid[0]) or self.anchor[1] + i >= len(grid):
                    return False
                if self.anchor[1] + i >= 0 and grid[self.anchor[1] + i][self.anchor[0] + j - 1] == 1:
                    return False
        return True

    def next_shape(self):
        d = iter(self.rotations)
        current_key = self.form

        for key in d:
            if key == current_key:
                next_key = next(d, None)
        return next_key

    def can_rotate(self, grid):
        next_shape = self.next_shape()
        for i in range(len(self.rotations[next_shape][self.rotation])):
            for j in range(len(self.rotations[next_shape][self.rotation][i])):
                x = self.anchor[0] + j
                y = self.anchor[1] + i

                if x < 0 or x >= len(grid[0]) or y >= len(grid):
                    return False

                if y >= 0 and grid[y][x] == 1:
                    return False
        return True

    def check_rotation(self):
        if self.rotation > len(self.rotations[self.form][self.rotation][0]) - 1:
            self.rotation = 0



    def move(self, grid):
        keys = pygame.key.get_pressed()
        if self.can_fall(grid):
            if (self.anchor[0] <= len(grid[0]) - len(self.shape[0]) - 1) and self.is_valid_right(grid):
                if keys[pygame.K_RIGHT]:
                    self.anchor[0] += 1
            if (self.anchor[0] > 0) and self.is_valid_left(grid):
                if keys[pygame.K_LEFT]:
                    self.anchor[0] -= 1


    def draw(self, surface, cells):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1 and self.anchor[1] + i >= 0: # BUFFER CHECK:
                    cube = pygame.draw.rect(surface, self.color, (cells[self.anchor[0]+j][self.anchor[1]+i][0], cells[self.anchor[0]+j][self.anchor[1]+i][1], self.size, self.size))
                    self.cubes.append(cube)
                    self.in_buffer = False
                else:
                    self.in_buffer = True

    def falling(self, grid, g):
        if self.can_fall(grid):
            self.anchor[1] += 1
        else:
            self.landed = True
            self.add_shape(grid, 0, 0)

    def rotate(self, grid):
        if self.can_rotate(grid):
            self.check_rotation()
            self.rotation += 1
            self.shape = self.rotations[self.form][self.rotation]


    def can_place(self, grid):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    x = self.anchor[0] + j
                    y = self.anchor[1] + i

                    if x < 0 or x >= len(grid[0]) or y >= len(grid):
                        return False

                    if y >= 0 and grid[y][x] == 1:
                        return False
        return True


