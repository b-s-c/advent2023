with open("input/10/real.txt") as f:
#with open("input/10/test.p2") as f:
#with open("input/10/test.p2.2") as f:
#with open("input/10/test.square") as f:
#with open("input/10/test.complex") as f:
    grid = [list(line.strip()) for line in f]

# buffer the grid
for i in range(0, len(grid)):
    grid[i].insert(0, '.')
    grid[i].append('.')
grid.insert(0, ['.' for _ in range(len(grid[0]))])
grid.append(['.' for _ in range(len(grid[0]))])
for line in grid:
    print(line)

upscale_dict = {
    "." : [['.','.','.'],['.','.','.'],['.','.','.']],
    "-" : [[' ',' ',' '],['-','-','-'],[' ',' ',' ']],
    "|" : [[' ','|',' '],[' ','|',' '],[' ','|',' ']],
    "F" : [[' ',' ',' '],[' ','F','-'],[' ','|',' ']],
    "7" : [[' ',' ',' '],['-','7',' '],[' ','|',' ']],
    "L" : [[' ','|',' '],[' ','L','-'],[' ',' ',' ']],
    "J" : [[' ','|',' '],['-','J',' '],[' ',' ',' ']],
    "S" : [[' ',' ',' '],['-','S',' '],[' ','|',' ']],
}

# upscale
upscaled_row = ['?' for _ in range(len(grid[0]) * 3)]
upscaled_grid = [list(upscaled_row) for _ in range(len(grid) * 3)]
for row in upscaled_grid:
    print(row)
for j in range(0, len(upscaled_grid), 3):
    for i in range(0, len(upscaled_grid[j]), 3):
        print("i = {}, j = {}".format(i, j))
        symbol = grid[j // 3][i // 3]
        for ia in range(0, 3):
            for ja in range(0, 3):
                upscaled_grid[j + ja][i + ia] = upscale_dict[symbol][ja][ia]
    for row in upscaled_grid:
        print("".join(row))
grid = upscaled_grid
with open("d10out.txt", "w") as w:
    for line in grid:
        w.write("".join(line))
        w.write('\n')

traverse_dict = {
    # relative to current point -> new point to scan
    "-": {
        (0, 1): (0, 2),
        (0, -1): (0, -2)
        },
    "|": {
        (1, 0): (2, 0),
        (-1, 0): (-2, 0)
        },
    "L": {
        (1, 0): (1, 1),
        (0, -1): (-1, -1)
        },
    "J": {
        (0, 1): (-1, 1),
        (1, 0): (1, -1)
        },
    "7": {
        (0, 1): (1, 1),
        (-1, 0): (-1, -1)
        },
    "F": {
        (0, -1): (1, -1),
        (-1, 0): (-1, 1)
        },
}

def find_start(grid) -> (int, int):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)
    return 555

def get_start_moves(grid, point) -> list[tuple[int]]:
    relative_points_to_check = ((0, 1), (0, -1), (1, 0), (-1, 0))
    points_to_return = []
    for rpc in relative_points_to_check:
        check_point = (point[0] + rpc[0], point[1] + rpc[1])
        check_symbol = grid[check_point[0]][check_point[1]]
        if check_symbol == '.' or check_symbol == ' ':
            continue
        if rpc in traverse_dict[check_symbol]:
            points_to_return.append([check_point, tuple(map(sum, zip(point, traverse_dict[check_symbol][rpc])))])
    return points_to_return

def get_move(grid, point, check_point) -> (int, int):
    check_symbol = grid[check_point[0]][check_point[1]]
    #print('current: {}, checking: {}'.format(point, check_point))
    #if check_symbol == '.':
    #    continue
    if check_symbol == 'S':
        return True, True
    if check_symbol == 'O':
        return True, True
    relative_point = (check_point[0] - point[0], check_point[1] - point[1])
    if relative_point in traverse_dict[check_symbol]:
        return check_point, tuple(map(sum, zip(point, traverse_dict[check_symbol][relative_point])))
    print(point, check_point, relative_point, check_symbol)

start_point = find_start(grid)
print("start point: {}".format(start_point))
start_moves = get_start_moves(grid, start_point)
print("start moves: {}".format(start_moves))

new_point, point_to_check = get_move(grid, start_moves[0][0], start_moves[0][1])
#print("new1: {}, to check: {}".format(new_point, point_to_check))
new_point2, point_to_check2 = get_move(grid, start_moves[1][0], start_moves[1][1])
#print("new2: {}, to check: {}".format(new_point2, point_to_check2))
#grid[new_point[0]][new_point[1]] = "+"
#grid[new_point2[0]][new_point2[1]] = "+"


with open("d10out.txt", "w") as w:
    for line in grid:
        w.write("".join(line))
        w.write('\n')
for line in grid:
    print(line)

count = 1
while 1:
    new_point, point_to_check = get_move(grid, new_point, point_to_check)
    #print("new1: {}, to check: {}".format(new_point, point_to_check))
    new_point2, point_to_check2 = get_move(grid, new_point2, point_to_check2)
    #print("new2: {}, to check: {}".format(new_point2, point_to_check2))
    count += 1
    grid[new_point[0]][new_point[1]] = "+"
    grid[new_point2[0]][new_point2[1]] = "+"
    if new_point == new_point2:
        count += 1
        break
print(count)

with open("d10out.txt", "w") as w:
    for line in grid:
        w.write("".join(line))
        w.write('\n')




count = 0
start_coord = (81, 57)
grid[start_point[0]+1][start_point[1]] = "+"
grid[start_point[0]+2][start_point[1]] = "+"
grid[start_point[0]][start_point[1]-1] = "+"
grid[start_point[0]][start_point[1]-2] = "+"
with open("d10out.txt", "w") as w:
    for line in grid:
        w.write("".join(line))
        w.write('\n')
#exit()
# flood fill
inspect = [start_coord]
while inspect:
    this_inspect = inspect.pop(0)
    coords_to_inspect = [
        [this_inspect[0]+1, this_inspect[1]],
        [this_inspect[0]-1, this_inspect[1]],
        [this_inspect[0]+1, this_inspect[1]+1],
        [this_inspect[0]+1, this_inspect[1]-1],
        [this_inspect[0]-1, this_inspect[1]+1],
        [this_inspect[0]-1, this_inspect[1]-1],
        [this_inspect[0], this_inspect[1] + 1],
        [this_inspect[0], this_inspect[1] - 1],
    ]
    for coords in coords_to_inspect:
        if grid[coords[0]][coords[1]] != "+" and grid[coords[0]][coords[1]] != "S":
            if grid[coords[0]][coords[1]] in traverse_dict.keys():
                count += 1
            if grid[coords[0]][coords[1]] == ".":
                count += 1/3
            inspect.append(coords)
            grid[coords[0]][coords[1]] = "+"#"█"
    #for line in grid:
        #print("".join(line))
    

print(count)
print(count/3)
print(count/9)
#for line in grid:
    #print("".join(line))
#with open("d10out.txt", "w") as w:
#    for line in grid:
#        w.write("".join(line))
#        w.write('\n')
