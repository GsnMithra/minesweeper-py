import os
import cv2
import pygame
import random

mines_map = set ()
def GenerateGrid (rows=50, cols=50, mine_count=random.randint (5, 15)):
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

resources_path = 'resources/'
mine = pygame.image.load (os.path.join (resources_path, 'mine.png'))
unrevealed = pygame.image.load (os.path.join (resources_path, 'unrevealed.png'))

red_flag = pygame.image.load (os.path.join (resources_path, 'flag_red.png'))
revealed = pygame.image.load (os.path.join (resources_path, 'revealed.png'))
numbers = [pygame.image.load (os.path.join (resources_path, image_path)) for image_path in os.listdir (resources_path) if len (image_path) == 5]

clock = pygame.time.Clock ()
cell_size = WINDOW_WIDTH // len(grid[0])

running = True
while running:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False
    
    for row in range (len (grid)):
        for col in range (len (grid[0])):
            cell_value = grid [row][col]
            if cell_value == 'M':
                window.blit (mine, (col * cell_size, row * cell_size))
            elif cell_value == 'E':
                window.blit (unrevealed, (col * cell_size, row * cell_size))

    window.fill ((184, 184, 184))
    pygame.display.flip ()
    clock.tick (60)
pygame.quit ()
