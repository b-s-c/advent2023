import itertools
import functools

inputs = []
with open("input/12/test.input") as f:
    for line in f:
        a, b = line.strip().split()
        inputs.append((a, tuple(map(int, b.split(',')))))

if 0:
    for i, inp in enumerate(inputs):
        pattern, values = inp
        pattern = "".join((([pattern] + ['?']) * 5))
        values = list(values) * 5
        inputs[i] = (pattern, values)
#for inp in inputs:
#    print(inp)

def check_match(pattern: str, values: list[int]) -> bool:
    patterns = [p for p in pattern.split('.') if p] # ...is not empty
    for i, v in enumerate(values):
        if len(patterns[i]) != v:
            return False
   # for i, p in enumerate(patterns):
   #     if len(p) != values[i]:
   #         return False
    return True

def can_place_spring(line, start, size) -> bool:
    # check that we won't go off the edge
    if start+size > len(line):
        return False
    # check to left and right
    left_sym = ''; right_sym = ''
    if start != 0:
        left_sym = line[start - 1]
        if line[start - 1] == '#':
            return False
    if start != len(line) - 1:
        if start + size < len(line):
            right_sym = line[start + size]
            if line[start + size] == '#':
                return False
    targeted_substring = line[start : start+size] 
    #print(targeted_substring)
    if len(set(targeted_substring)) == 1 and '#' in targeted_substring: # accept 'overwriting' a currently existing set of hashes
        #print(left_sym, right_sym)
        if (left_sym == '.' or left_sym == '?' or left_sym == '') and (right_sym == '.' or right_sym == '?' or right_sym == ''):
            return True
    if '.' in targeted_substring:
        return False
    if '#' in targeted_substring:
        return False
    return True

def place_spring(line, start, size) -> str:
    line = list(line)
    for i in range(start, start+size):
        line[i] = '#'
    if start != 0:
        line[start - 1] = '.'
    if start + size < len(line):
        line[start + size] = '.'
    return "".join(line)

@functools.cache
def get_placements(line, size):
    valid_placements = []
    for start in range(len(line)):
        can_place = can_place_spring(line, start, size)
        if can_place:
            valid_placements.append(start)
        #print(start, size, can_place)
    #print(valid_placements, len(valid_placements))
    placements = []
    for placement in valid_placements:
        with_dots = place_spring(line, placement, size)
        if check_match(with_dots, [size]):
            placements.append((with_dots, placement + size))
    return placements

for inp in inputs:
    line, sizes = inp
    size = sizes[0]
    #print(inp)
    placements = get_placements(line, size)
    #print(placements)
    for potential in placements:
        remaining_line = potential[0][potential[1]:]
        #print(remaining_line)
    #print()
    num_placements = len(placements)

tracker = {}
def recurse(line, values):
    print(line, values)
    key = (line, values)
    if key in tracker:
        print('returning {}'.format(tracker[key]))
        return tracker[key]
    if len(values) == 1:
        size = values[0]
        num_placements = len(get_placements(line, size))
        tracker[key] = num_placements
        print('returning {}'.format(num_placements))
        return num_placements
    else:
        size = values[0]
        placements = get_placements(line, size)
        if len(placements) == 0:
            return 0
        tracker[(line, values)] = sum(recurse(potential[0][potential[1]:], values[1:]) for potential in placements)
        print('returning {}'.format(tracker[(line, values)]))
        return tracker[(line, values)]

p2_total = 0
for inp in inputs:
    p2_total += recurse(*inp)
    print()
print(p2_total)
    