import itertools
import functools

inputs = []
with open("input/12/test.input") as f:
    for line in f:
        a, b = line.strip().split()
        inputs.append((a, tuple(map(int, b.split(',')))))

#for inp in inputs:
#    print(inp)

@functools.cache
def check_match(pattern: str, values: list[int]) -> bool:
    patterns = [p for p in pattern.split('.') if p] # ...is not empty
    for i, p in enumerate(patterns):
        if len(p) != values[i]:
            return False
    return True

def apply_to_pattern(pattern: str, permutation: str) -> str:
    pattern = list(pattern)
    permutation = list(permutation)
    replacement_count = 0
    for i, char in enumerate(pattern):
        if char == '?':
            pattern[i] = permutation[replacement_count]
            replacement_count += 1
    return "".join(pattern)

def place_hashes(size, count): # thanks https://stackoverflow.com/a/43817007
    for positions in itertools.combinations(range(size), count):
        p = ['.'] * size
        for i in positions:
            p[i] = '#'
        yield p

#print(check_match('#.#.###', [1,1,3]))
#print(check_match('.#...#....###.', [1,1,3]))
#print(check_match('.#.###.#.######', [1,3,1,6]))
#print(check_match('####.#...#...', [4,1,1]))
#print(check_match('#....######..#####.', [1,6,5]))
#print(check_match('.###.##....#', [3,2,1]))

p1_count = 0
for inp in inputs:
    working_count = 0
    print(inp)
    pattern, values = inp
    max_hashes_to_add = sum(values) - list(pattern).count('#')
    missing_spaces = list(pattern).count('?')
    permutations = list(place_hashes(missing_spaces, max_hashes_to_add))
    #print(permutations)
    for p in permutations:
        pattern_to_check = apply_to_pattern(pattern, p)
        works = check_match(pattern_to_check, values)
        #print(pattern, p)
        #print(pattern_to_check)
        #print(works)
        if works:
            working_count += 1
    p1_count += working_count

print(p1_count)

for i, inp in enumerate(inputs):
    pattern, values = inp
    pattern = "".join(([pattern] + ['?']) * 5 )
    values = tuple(list(values) * 5)
    inputs[i] = (pattern, values)
