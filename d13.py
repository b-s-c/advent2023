from functools import cache

with open('input/13/real.input') as f:
    lines = [line.strip() for line in f] + ['']

inputs = []
this_input = []
while lines:
    line = lines.pop(0)
    if len(line) != 0:
        this_input.append(line)
        continue
    inputs.append(this_input)
    this_input = []
    
def get_row(puzzle, row):
    return puzzle[row]

def get_column(puzzle, column):
    return [row[column] for row in puzzle]

@cache
def is_mirror(one: tuple, two: tuple):
    #print(one, two)
    one = list(one)
    two = list(two)
    min_length = min(len(one), len(two))
    one = one[-min_length:]
    two = two[0:min_length]
    one.reverse()
    #print(one, two)
    for i in range(min_length):
        if one[i] != two[i]:
            #print('false\n')
            return False
    #print('true\n')
    return True

total = 0
for inp in inputs:
    for line in inp:
        print(line)
    
    potential_column_splits = set(range(1, len(inp[0])))
    for row in inp:
        splits_to_remove = set()
        for p_s in potential_column_splits:
            one = row[0:p_s]
            two = row[p_s:]
            if not is_mirror(one, two):
                splits_to_remove.add(p_s)
        potential_column_splits.difference_update(splits_to_remove)

    #print(f'col splits: {potential_column_splits}')
    #print()
    column_split = potential_column_splits.pop() if potential_column_splits else 0
    print(f'column split: {column_split}')
    total += column_split

    potential_row_splits = set(range(1, len(inp)))
    for column in [get_column(inp, i) for i in range(0, len(inp[0]))]:
        #print(f'column: {column}')
        splits_to_remove = set()
        for p_s in potential_row_splits:
            one = tuple(column[0:p_s])
            two = tuple(column[p_s:])
            if not is_mirror(one, two):
                splits_to_remove.add(p_s)
        potential_row_splits.difference_update(splits_to_remove)

    #print(f'row splits: {potential_row_splits}')
    #print()
    row_split = potential_row_splits.pop() if potential_row_splits else 0

    print(f'row split: {row_split}')
    total += row_split * 100

    if len(potential_row_splits) > 0 or len(potential_column_splits) > 0:
        print(f'remaining row splits: {potential_row_splits}')
        print(f'remaining col splits: {potential_column_splits}')
        input()
    if row_split > 0 and column_split > 0:
        input()
    print() 

print(total)
