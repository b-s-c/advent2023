with open("test.input") as f:
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
        print("inserted column at {}".format(i))

#for line in grid:
#    print(line)
#print()

row_to_insert = [str('.') for _ in range(0, len(grid[0]))]
for row in [row for row in range(len(galaxy_in_row) -1, -1, -1) if galaxy_in_row[row] == False]:
    grid.insert(row, "".join(row_to_insert))
    print("inserted row at {}".format(row))

for line in grid:
    print(line)
print()
