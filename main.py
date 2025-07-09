import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = WINDOW_WIDTH // BLOCK_SIZE
ROWS = WINDOW_HEIGHT // BLOCK_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
]

# Tetromino shapes
SHAPES = {
    "I": [[1, 1, 1, 1]],
    "J": [[1, 0, 0], [1, 1, 1]],
    "L": [[0, 0, 1], [1, 1, 1]],
    "O": [[1, 1], [1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 1]],
}


class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def get_cells(self):
        return [(self.x + col, self.y + row)
                for row, line in enumerate(self.shape)
                for col, cell in enumerate(line) if cell]


class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_piece = self.get_new_piece()
        self.drop_time = 0
        self.game_over = False

    def get_new_piece(self):
        shape_name = random.choice(list(SHAPES.keys()))
        shape = SHAPES[shape_name]
        color = random.choice(COLORS)
        return Tetromino(shape, color)

    def valid_move(self, shape, x, y):
        for row, line in enumerate(shape):
            for col, cell in enumerate(line):
                if cell:
                    nx, ny = x + col, y + row
                    if nx < 0 or nx >= COLUMNS or ny >= ROWS:
                        return False
                    if ny >= 0 and self.grid[ny][nx] != BLACK:
                        return False
        return True

    def lock_piece(self, piece):
        for x, y in piece.get_cells():
            if y < 0:
                self.game_over = True
            else:
                self.grid[y][x] = piece.color
        self.clear_lines()
        self.current_piece = self.get_new_piece()

    def clear_lines(self):
        self.grid = [row for row in self.grid if BLACK in row]
        while len(self.grid) < ROWS:
            self.grid.insert(0, [BLACK for _ in range(COLUMNS)])

    def move(self, dx, dy):
        new_x = self.current_piece.x + dx
        new_y = self.current_piece.y + dy
        if self.valid_move(self.current_piece.shape, new_x, new_y):
            self.current_piece.x = new_x
            self.current_piece.y = new_y
        elif dy == 1:
            self.lock_piece(self.current_piece)

    def rotate(self):
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if not self.valid_move(self.current_piece.shape, self.current_piece.x, self.current_piece.y):
            self.current_piece.shape = old_shape

    def draw_grid(self):
        for y in range(ROWS):
            for x in range(COLUMNS):
                pygame.draw.rect(self.screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
                if self.grid[y][x] != BLACK:
                    pygame.draw.rect(self.screen, self.grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_piece(self):
        for x, y in self.current_piece.get_cells():
            if y >= 0:
                pygame.draw.rect(self.screen, self.current_piece.color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def run(self):
        while not self.game_over:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)

            self.drop_time += 1
            if self.drop_time > 30:
                self.move(0, 1)
                self.drop_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    elif event.key == pygame.K_UP:
                        self.rotate()

            self.draw_grid()
            self.draw_piece()
            pygame.display.update()

        print("Game Over")
        pygame.quit()


if __name__ == "__main__":
    Tetris().run()
