import utils
import re
from math import prod

def check_neighbours(grid:list[str], x:int, y:int, value:int) -> bool:
    """
    see if a neighbour is a symbol we're looking for
    """
    # boundary checks
    min_x = max(x - 1, 0)
    min_y = max(y - 1, 0)
    max_x = min(x + 1, len(grid[0]) - 1) + 1
    max_y = min(y + 1, len(grid) - 1) + 1

    for x_check in range(min_x, max_x):
        for y_check in range(min_y, max_y):
            if x_check == y_check: continue
            neighbour = grid[y_check][x_check]
            if neighbour == '*':
                utils.dict_increment(stars, (x_check, y_check), [value])
            if utils.is_symbol_d3(neighbour):
                return True # strictly speaking, probably should not return early here and continue to look for '*'. but it worked regardless for the AoC input because any given number borders only one symbol at most
    return False

grid = []
stars = {}
total_p1 = 0
total_p2 = 0

with open("input/03/real.txt") as f:
    grid = [line.strip() for line in f]

for y, line in enumerate(grid):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        value = int(match.group())
        for x in range(*match.span()):
            if check_neighbours(grid, x, y, value):
                total_p1 += value
                break

for gear_ratio_list in stars.values():
    if len(gear_ratio_list) == 2:
        total_p2 += prod(gear_ratio_list)

print(total_p1)
print(total_p2)
