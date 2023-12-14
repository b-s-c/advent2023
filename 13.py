#!/usr/bin/env python3

"""
not my work
"""

file = "input/13/real.input"
#file = "test"

with open(file) as f:
    data = f.read().split("\n\n")

def check_horiz(grid, pairs):
    n_smudge = 0
    for (row1, row2) in pairs:
        for col in range(len(grid[row1])):
            if grid[row1][col] != grid[row2][col]:
                n_smudge += 1
    return n_smudge

def check_vert(grid, pairs):
    n = len(grid)
    n_smudge = 0
    for (col1, col2) in pairs:
        for i in range(n):
            if grid[i][col1] != grid[i][col2]:
                n_smudge += 1
    return n_smudge

def generate_pairs(start_axe, n):
    pairs = []
    for k in range(n):
        low = start_axe-k
        high = start_axe+k+1
        if low < 0 or high >= n:
            return pairs
        pairs.append((low, high))

def find_reflection(grid, n_authorized_smudge):
    grid = grid.strip().split()
    n = len(grid)
    m = len(grid[0])

    # find horizontal reflection
    for row in range(n):
        pairs = generate_pairs(row, n)
        #print(f'pairs: {pairs}')
        if len(pairs) == 0:
            continue
        #print("--", row, pairs)
        n_smudge = check_horiz(grid, pairs)
        if n_smudge == n_authorized_smudge:
            print("found horiz reflex", row)
            return 100 * (row+1)

    # find vertical reflections
    for col in range(m):
        pairs = generate_pairs(col, m)
        if len(pairs) == 0:
            continue
        #print("--", col, pairs)
        n_smudge = check_vert(grid, pairs)
        if n_smudge == n_authorized_smudge:
            print("found vert reflex", col)
            return col+1

    print("error", grid)
    return None

s = sum(find_reflection(block, 0) for block in data)
print(s)
s = sum(find_reflection(block, 1) for block in data)
print(s)
