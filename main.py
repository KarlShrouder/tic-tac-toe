from classes import *

pygame.init()

clock = pygame.time.Clock()
grid = Grid(init_grid_cells())
game_window = pygame.display.set_mode((700, 400))

while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()

        if i.type == pygame.MOUSEBUTTONUP:
            quit()

    for i in grid.cells:
        i.update()

    grid.draw(game_window)

    clock.tick(FRAMES_PER_SECOND)
    pygame.display.update()
