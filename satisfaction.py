#/usr/bin/python3
import pygame, sys, random, sortingAlgorithms, copy, colorsys

pygame.init()

screen = pygame.display.set_mode((1600, 900))

"""Create the background"""
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

pixelSize = 10
gridHeight = int((900-20)/pixelSize)
gridWidth = int((1600-20)/pixelSize)
grid = [[0 for x in range(gridHeight)] for y in range(gridWidth)] 
sorter = [0 for x in range(gridWidth)] 
offsetX = 10
offsetY = 10

sort = sortingAlgorithms.random_sort()
for x in range(len(grid)):
    for y in range(len(grid[x])):
        grid[x][y] = (y/float(len(grid[x])))
    random.shuffle(grid[x])
    sorter[x] = sort(grid[x])

lastGrid = copy.deepcopy(grid)
background.fill(0x000000)
first = True

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    for x in range(gridWidth):
        try:
            next(sorter[x])
        except StopIteration as e:
            pass
        for y in range(gridHeight):
            if grid[x][y] != lastGrid[x][y] or first:
                col = pygame.Color(0)
                col.hsva = (grid[x][y]*360, 100, 100, 100)
                pygame.display.update(
                    pygame.draw.rect(screen, col, (x*pixelSize+offsetX, y*pixelSize+offsetY, pixelSize, pixelSize)))
                lastGrid[x][y] = grid[x][y]
    
    first = False
    #pygame.display.flip()

    clock.tick(60)
    print(clock.get_fps())
    #screen.blit(background, (0,0))