from math import lcm

path = ""
routing = {}
starting_node = "AAA"
with open("input/08/real.txt") as f:
    lines = f.readlines()
    path = lines[0].strip()
    routing = {}
    for line in lines[2:]:
        line = line.strip()
        start, dest = line.split(' = ')
        dest1, dest2 = dest.split(', ')
        dest1 = dest1[1:]
        dest2 = dest2[:-1]
        routing[start] = (dest1, dest2)

direction_dict = {'L': 0, 'R': 1}

def walk(starting_node: str, target_nodes: list[str]) -> int:
    steps = 0
    current_node = starting_node
    while 1:
        for direction in path:
            current_node = routing[current_node][direction_dict[direction]]
            steps += 1
            if current_node in target_nodes:
                return steps

a_nodes = [node for node in routing.keys() if node[2] == 'A']
z_nodes = [node for node in routing.keys() if node[2] == 'Z']

walk_lengths = []
for node in a_nodes:
    walk_lengths.append(walk(node, z_nodes))

print(walk('AAA', ['ZZZ'])) # p1
print(lcm(*walk_lengths)) # p2
