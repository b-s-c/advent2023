from itertools import combinations

with open("input/11/real.input") as f:
    grid = [line.strip() for line in f.readlines()]

#for line in grid:
#    print(line)
#print()

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
expanded_row_set = {row for row in range(0, len(galaxy_in_row)) if galaxy_in_row[row] == False}
expanded_column_set = {column for column in range(0, len(galaxy_in_column)) if galaxy_in_column[column] == False}
#print(expanded_row_set)
#print(expanded_column_set)

#for line in grid:
#    print(line)
#print()

galaxy_dict = {}
galaxy_id = 1
for j, row in enumerate(grid):
    for i, item in enumerate(row):
        if item == "#":
            galaxy_dict[galaxy_id] = (j, i)
            galaxy_id += 1

#print(galaxy_dict, '\n')

combos = [c for c in combinations(galaxy_dict.keys(), 2)]
#print(combos, len(combos))

sum_of_distances = 0
for combo in combos:
    p1 = list(galaxy_dict[combo[0]])
    p2 = list(galaxy_dict[combo[1]])
    column_offset = 0
    row_offset = 0
    #how_many_times_larger = 2
    #how_many_times_larger = 10
    #how_many_times_larger = 100
    how_many_times_larger = 1000000
    for column_to_expand in expanded_column_set:
        if column_to_expand > min(p1[1], p2[1]) and column_to_expand < max(p1[1], p2[1]):
            column_offset += how_many_times_larger - 1
    for row_to_expand in expanded_row_set:
        if row_to_expand > min(p1[0], p2[0]) and row_to_expand < max(p1[0], p2[0]):
            row_offset += how_many_times_larger - 1
    

    result = (max(p1[0], p2[0]) - min(p1[0], p2[0])) + (max(p1[1], p2[1]) - min(p1[1], p2[1])) + row_offset + column_offset
    #result = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])# + row_offset + column_offset
    #print("Between galaxy {} {} and galaxy {} {} with offsets ({}, {}): {}".format(combo[0], p1, combo[1], p2, row_offset, column_offset, result))
    #print("Between galaxy {} {} and galaxy {} {}: {}".format(combo[0], p1, combo[1], p2, result))
    sum_of_distances += result 
print(sum_of_distances, f'({len(combos)} combos)')
