import utils
import re
from math import prod

def check_neighbour(grid:list[str], x:int, y:int, value:int) -> bool:
    """
    see if a neighbour is a symbol we're looking for
    """
    if x < 0 or x >= grid_width or y < 0 or y >= grid_height:
        return None
    neighbour = grid[y][x]
    if neighbour == '*':
        utils.dict_increment(stars, (x, y), [value])
        return True
    if neighbour != '.' and not neighbour.isdigit():
        return True

grid = []
stars = {}
total_p1 = 0
total_p2 = 0

with open("input/03/big.txt") as f:
    grid = [line.strip() for line in f]
grid_height = len(grid)
grid_width = len(grid[0]) # assuming grid is perfectly rectangular

for y, line in enumerate(grid):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        value = int(match.group())
        x1, x2 = match.span() # x1 inclusive, x2 exclusive
        results = {check_neighbour(grid, x1 - 1, y, value), check_neighbour(grid, x2, y, value)} # left and right
        for x in range(x1 - 1, x2 + 1):
            results.add(check_neighbour(grid, x, y - 1, value)) # row above
            results.add(check_neighbour(grid, x, y + 1, value)) # row below
        if True in results:
            total_p1 += value

for gear_ratio_list in stars.values():
    if len(gear_ratio_list) == 2:
        total_p2 += prod(gear_ratio_list)

print(total_p1)
print(total_p2)
