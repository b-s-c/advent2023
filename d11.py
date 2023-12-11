from itertools import combinations

with open("real.input") as f:
    grid = [line.strip() for line in f.readlines()]

for line in grid:
    print(line)
print()

galaxy_in_column = [False for _ in range(len(grid[0]))]
galaxy_in_row = [False for _ in range(len(grid))]
for j, row in enumerate(grid):
    if '#' in row:
        galaxy_in_row[j] = True
    for i, point in enumerate(row):
        if point != '.':
            galaxy_in_column[i] = True

#print("Row: {}".format(galaxy_in_row))
#print("Column: {}".format(galaxy_in_column))
#print()

for i in [column for column in range(len(galaxy_in_column) - 1, -1, -1) if galaxy_in_column[column] == False]:
    for j, _ in enumerate(grid):
        grid[j] = list(grid[j])
        grid[j].insert(i, '.')
        grid[j] = "".join(grid[j])
        #print("inserted column at {}".format(i))

#for line in grid:
#    print(line)
#print()

row_to_insert = ['.' for _ in range(0, len(grid[0]))]
for row in [row for row in range(len(galaxy_in_row) -1, -1, -1) if galaxy_in_row[row] == False]:
    grid.insert(row, "".join(row_to_insert))
    #print("inserted row at {}".format(row))

for line in grid:
    print(line)
print()

galaxy_dict = {}
galaxy_id = 1
for j, row in enumerate(grid):
    for i, item in enumerate(row):
        if item == "#":
            galaxy_dict[galaxy_id] = (j, i)
            galaxy_id += 1

print(galaxy_dict, '\n')

combos = [c for c in combinations(galaxy_dict.keys(), 2)]
print(combos, len(combos))

sum_of_distances = 0
for combo in combos:
    p1 = galaxy_dict[combo[0]]
    p2 = galaxy_dict[combo[1]]
    result = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    sum_of_distances += result 
print(sum_of_distances)
