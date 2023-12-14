from functools import cache

with open("input/14/real.input") as f:
    grid = [list(line.strip()) for line in f]
height = len(grid)
width = len(grid[0])

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

#print_grid(grid)

def get_tilted_position(grid, row, column, direction='n'):
    highest_point = (-1, -1)
    r_it = range(row, row + 1)
    c_it = range(column, column + 1)
    match direction:
        case 'n':
            r_it = range(row - 1, -1, -1)
        case 's':
            r_it = range(row + 1, height)
        case 'e':
            c_it = range(column + 1, width)
        case 'w':
            c_it = range(column - 1, -1, -1)
    for r in r_it:
        for c in c_it:
            item = grid[r][c]
            #print(f'checking ({r}, {c}): {item}')
            if item == '.':
                highest_point = (r, c)
            else:
                #print(f'returning {highest_point}')
                return highest_point
    #print(f'returning {highest_point}')
    return highest_point

def rock_tilt(grid, direction) -> list[str]:
    # north: start top - 1, go to bottom
    # south: start bottom - 1, go to top
    h_it = range(0, height)
    w_it = range(0, width)
    match direction:
        case 'n':
            h_it = range(1, height)
        case 's':
            h_it = range(height - 1, -1, -1)
        case 'e':
            w_it = range(width - 1, -1, -1)
        case 'w':
            w_it = range(1, width)
    for h in h_it:
        for w in w_it:
            item = grid[h][w]
            if item != 'O':
                continue
            #print(f'O at {h},{w}')
            (p1, p2) = get_tilted_position(grid, h, w, direction)
            if p1 != -1:
                grid[h][w] = '.'
                grid[p1][p2] = 'O'

def cycle(grid):
    rock_tilt(grid, 'n')
    rock_tilt(grid, 'w')
    rock_tilt(grid, 's')
    rock_tilt(grid, 'e')
    return grid

def get_load(grid):
    total = 0
    height = len(grid)
    for h, row in enumerate(grid):
        factor = height - h
        total += factor * row.count('O')
    return total

grids = {}
for i in range(1, 10000):
    grid = cycle(grid)
    if str(grid) in grids:
        print(f'found at cycle {i}, matching cycle {grids[str(grid)]}')
        cycle_len = i - grids[str(grid)]
        start = grids[str(grid)]
        print(f'cycle start = {start}')
        print(f'cycle_len = {cycle_len}')
        search_value = (1000000000 - start) % cycle_len
        #print(get_load(grid))
        print(f'search_value = {search_value}')
        input()
        break
    grids[str(grid)] = i

for i in range(start, start + search_value):
    grid = cycle(grid)
    print(i + 1, get_load(grid))
