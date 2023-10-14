import os
import cv2
import pygame
import random
from algorithm import updateBoard

mines_map = set ()
red_flag_map = set ()

def GenerateGrid (rows=15, cols=15, mine_count=random.randint (20, 35)):
    grid = [['E' for _ in range (cols)] for _ in range (rows)]
    for i in range (mine_count):
        row = random.randint (0, rows - 1)
        col = random.randint (0, cols - 1)
        grid [row][col] = 'M'
        mines_map.add ((row, col))
    return grid

pygame.init ()
WINDOW_WIDTH, WINDOW_HEIGHT = (650, 650)
window = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption ('Minesweeper')

grid = GenerateGrid ()
cell_size = min (WINDOW_WIDTH // len (grid[0]), WINDOW_HEIGHT // len (grid))

resources_path = 'resources/'
mine = pygame.image.load (os.path.join (resources_path, 'mine.png'))
unrevealed = pygame.image.load (os.path.join (resources_path, 'unrevealed.png'))

red_flag = pygame.image.load (os.path.join (resources_path, 'flag_red.png'))
revealed = pygame.image.load (os.path.join (resources_path, 'revealed.png'))
numbers = [pygame.image.load (os.path.join (resources_path, f'{i + 1}.png')) for i in range (7)]

mine = pygame.transform.scale (mine, (cell_size, cell_size))
unrevealed = pygame.transform.scale (unrevealed, (cell_size, cell_size))
red_flag = pygame.transform.scale (red_flag, (cell_size, cell_size))
revealed = pygame.transform.scale (revealed, (cell_size, cell_size))
numbers = [pygame.transform.scale (number, (cell_size, cell_size)) for number in numbers]

image_map = {
    'M': unrevealed,
    'E': unrevealed,
    'B': revealed,
    'X': mine,
    'R': red_flag
}

clock = pygame.time.Clock ()

running = True
while running:
    if red_flag_map == mines_map:
        running = False
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos ()
        col = x // cell_size
        row = y // cell_size
        if event.button == 1:
            grid = updateBoard (grid, (row, col))
        if event.button == 3:
            if grid[row][col] == 'E' or grid[row][col] == 'M':
                grid[row][col] = 'R'
                red_flag_map.add ((row, col))
            elif grid[row][col] == 'R':
                if (row, col) in mines_map:
                    grid[row][col] = 'M'
                else:
                    grid[row][col] = 'E'
                red_flag_map.remove ((row, col))

    for row in range (len (grid)):
        for col in range (len (grid[0])):
            cell_value = grid [row][col]
            x = col * cell_size
            y = row * cell_size

            if not cell_value.isdigit ():
                window.blit (image_map [cell_value], (x, y))
            else:
                window.blit (numbers [int (cell_value) - 1], (x, y))

    pygame.display.flip ()
    clock.tick (60)
pygame.quit ()
