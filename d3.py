import utils
import re

def check_neighbours(grid:list[str], x:int, y:int, value:int) -> bool:
    """
    see if a neighbour is a symbol we're looking for
    """
    # boundary checks
    min_x = max(x - 1, 0)
    min_y = max(y - 1, 0)
    max_x = min(x + 1, len(grid[0]) - 1)
    max_y = min(y + 1, len(grid) - 1)

    for x_check in range(min_x, max_x + 1):
        for y_check in range(min_y, max_y + 1):
            #print("[{}, {}]: {}".format(x_check, y_check, grid[y_check][x_check]))
            neighbour = grid[y_check][x_check]
            if neighbour == '*':
                utils.dict_increment(stars, (x_check, y_check), [value])
            if utils.is_symbol_d3(neighbour):
                return True # not 100% sure, but strictly speaking, probably should not return early here and continue to look for '*'. but it worked regardless
    return False

grid = []
stars = {}
total_p1 = 0
with open("input/03/real.txt") as f:
    grid = [line.strip() for line in f]

for y, line in enumerate(grid):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        span = match.span()
        value = int(match.group())
        valid = False
        for x in range(span[0], span[1]):
            valid = check_neighbours(grid, x, y, value)
            if valid: break
        if valid:
            total_p1 += value

total_p2 = 0
from math import prod
for gear_ratio_list in stars.values():
    if len(gear_ratio_list) == 2:
        total_p2 += prod(gear_ratio_list)

print(total_p1)
print(total_p2)
