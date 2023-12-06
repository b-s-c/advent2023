"""
maps: destination range start, source range start, range length
e.g. 50 98 2
     d[50, 51]
     s[98, 99]

e.g. 52 50 48
     d[52, 53, 54, ..., 98, 99]
     s[50, 51, 52, ..., 96, 97]
"""

category_map = { # also the index of these in `maps`
    "s":0,
    "seed-to-soil":1,
    "soil-to-fertilizer":2,
    "fertilizer-to-water":3,
    "water-to-light":4,
    "light-to-temperature":5,
    "temperature-to-humidity":6,
    "humidity-to-location":7,
}

def binary_search(d:dict, v:int) -> int:
    lst_ranges = list(d.keys())
    #print(lst_ranges, v)
    high = len(lst_ranges) - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        #print(low,mid,high)
        if is_num_in_x_y(v, *lst_ranges[mid]):
            #print("found in {}".format(lst_ranges[mid]))
            return d[lst_ranges[mid]]
        if v < lst_ranges[mid][0]:
            high = mid - 1
            continue
        if v > lst_ranges[mid][0]:
            low = mid + 1
            continue
        raise("oops")
    return -1

def is_num_in_x_y(num:int, x:int, y:int) -> bool:
    if num >= x and num <= y:
        return True
    return False

def range_intersection(a:tuple, b:tuple, inc=0):
    print("finding intersect between {} and {}".format(a, b))
    if a[0] > b[1] or a[1] < b[0]:
        return -1
    if a[0] > a[1] or b[0] > b[1]:
        raise("bad range in {} or {}".format(a, b))
    left = [-1, -1]
    intersect = [-1, -1]
    right = [-1, -1]
    if is_num_in_x_y(a[0], *b):
        intersect[0] = a[0]
        intersect[1] = min(a[1], b[1])
        if is_num_in_x_y(a[1], *b):
            return [[], [seed + inc for seed in intersect], []]
    elif is_num_in_x_y(b[0], *a):
        intersect[0] = b[0]
        intersect[1] = min(a[1], b[1])
    if a[0] < intersect[0]:
        left = [a[0], intersect[0] - 1]
    if a[1] > intersect[1]:
        right = [intersect[1] + 1, a[1]]
    if a[0] == intersect[0]:
        left = []
    if a[1] == intersect[1]:
        right = []
    intersect = [seed + inc for seed in intersect]
    return [left, intersect, right]
    
#a = (61, 68)
#b = (45, 63)
#a = (55, 68)
#b = (53, 60)
#a = (1, 10)
#b = (10, 15)
#a = (1, 20)
#b = (5, 10)
#inte = range_intersection(a, b)
#print(inte)
#exit()

maps = [[] for _ in range(8)]
with open("input/05/real.txt") as f:
    category = -1
    for line in f:
        line = line.strip()
        if not line: continue
        if ':' in line:
            category = category_map[line.split(':')[0].strip()[:-4]]
            if category != 0: continue # seeds has no newline :/
        match category:
            case 0:
                maps[category] = tuple(map(int, line.split(':')[1].strip().split()))
            case _:
                maps[category].append((tuple(map(int, line.strip().split()))))
#print(maps)

ranges = [{}]
for i, this_map in enumerate(maps):
    if i == 0: continue
    sd_dict = {}
    for single_mapping in this_map:
        sd_dict[((single_mapping[1], single_mapping[1] + single_mapping[2] - 1))] = single_mapping[0] - single_mapping[1]
    sd_dict = {k: v for k, v in sorted(sd_dict.items(), key=lambda item: item[0][0])}
    ranges.append(sd_dict)

for d in ranges:
    #print(d)
    for k, v in d.items():
        print(k, v)
    print()


seed_ranges = []
for i in range(0, len(maps[0]), 2):
    seed_ranges.append((maps[0][i], maps[0][i] + maps[0][i+1]))
seed_ranges.sort()
print(seed_ranges)
from sys import maxsize
smallest = maxsize

#for r in seed_ranges:
#    print("starting {}".format(r))
#    for seed in range(*(r)):
#        value = seed
#        flag = 0
#        #print("starting value: {}".format(value))
#        for stage in range(1, 8):
#            sd_dict = ranges[stage]
#            #print(sd_dict)
#            found = binary_search(sd_dict, value)
#            if found == -1:
#                continue
#            else:
#                value += found
#            #print(value)
#        smallest = min(smallest, value)
#print(smallest)

new_seed_ranges = []
for map_dict in ranges[1:]:
    new_seed_ranges = []
    print('d', map_dict)
    print('sr', seed_ranges)
    print('r',ranges)
    print("seed ranges count: {}".format(len(seed_ranges)))
    for i in range(len(seed_ranges)):
        s_r = seed_ranges[i]
        #map_dict = ranges[1]
        #print(list(map_dict.keys()))
        success = 0
        for map_dict_key in list(map_dict.keys()):
            print("[{}, {}] in [{}, {}] for {}".format(s_r[0], s_r[1], map_dict_key[0], map_dict_key[1], map_dict[map_dict_key]))
            result = range_intersection(s_r, map_dict_key, map_dict[map_dict_key])
            if result == -1 or result == -5:
                pass
            else:
                success = 1
                print(result)
                for r in result:
                    if r:
                        new_seed_ranges.append(r)
            print()
        if not success:
            new_seed_ranges.append(s_r)
    new_seed_ranges=sorted(new_seed_ranges)
    #print("new: {}".format(new_seed_ranges))
    seed_ranges = new_seed_ranges
    #print()
print(new_seed_ranges[0])
