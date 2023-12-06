import copy
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

def is_num_in_x_y(num:int, x:int, y:int) -> bool:
    if num >= x and num <= y:
        return True
    return False

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

def range_intersection(a:tuple, b:tuple, inc=0):
    # a fits into b (or is the same):
    # [4, 5] into [1, 10]
    if a[0] >= b[0] and a[1] <= b[1]:
        #print("1")
        return [[], [a[0]+inc, a[1]+inc], []]

    # overlap by 1
    # [1, 3] into [3, 5] --> [1, 2], [3, 3], [4, 5]
    if a[1] == b[0]:
        #print("8")
        overlap = [a[1], b[0] - 1]
        start = [a[0], a[1]]
        end = [b[0] + 1, b[1]]
        return [start, overlap, end]

    # a is totally out of range of b:
    # [1, 2] into [5, 6]
    if a[0] < b[0] and a[1] < b[0]:
        #print("2")
        return -5
    # [5, 6] into [1, 2]
    if a[0] > b[1]:
        #print("3")
        return -5

    # a consumes b
    # [1, 10] into [3, 4] --> [1, 2], [3, 4], [5, 10]
    if b[0] >= a[0] and b[1] <= a[1]:
        #print("7")
        start = [a[0], b[0] - 1]
        overlap = [b[0] + inc, b[1] + inc]
        end = [b[1] + 1, a[1]]
        return [start, overlap, end]

    # a overlaps into b start
    # [5,10] into [7, 15] --> [5, 6], [7, 10], [11, 15]
    if a[0] < b[0] and a[1] >= b[0]:
        #print("4")
        overlap = [b[0] + inc, a[1] + inc]
        start = [a[0], b[0]]
        end = [a[1], b[1]]
        return [start, overlap, end]

    # a consumes b
    # [9,14] into [6,11] --> [6, 8], [9, 11], [12, 14]
    if a[0] >= b[0] and a[1] >= b[1]:
        #print("5")
        overlap = [a[0] + inc, b[1] + inc]
        start = [b[1], a[0] - 1]
        end = [b[1] + 1, a[1]]
        return [start, overlap, end] 

    # a overlaps onto b end
    # [10,14] into [6,11] --> [6, 9], [10, 11], [12, 14]
    if a[0] <= b[1] and a[1] > b[1]:
        #print("6")
        overlap = [a[0] + inc, b[1] + inc]
        start = [b[0], a[0] - 1]
        end = [b[1] + 1, a[1]]
        return [start, overlap, end]









    return None
    return -1

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
    #print('d', map_dict)
    #print('sr', seed_ranges)
    #print('r',ranges)
    #print("seed ranges count: {}".format(len(seed_ranges)))
    for i in range(len(seed_ranges)):
        s_r = seed_ranges[i]
        #map_dict = ranges[1]
        #print(list(map_dict.keys()))
        success = 0
        for map_dict_key in list(map_dict.keys()):
            #print("[{}, {}] in [{}, {}] for {}".format(s_r[0], s_r[1], map_dict_key[0], map_dict_key[1], map_dict[map_dict_key]))
            result = range_intersection(s_r, map_dict_key, map_dict[map_dict_key])
            if result == -1 or result == -5:
                pass
            else:
                success = 1
                #print(result)
                for r in result:
                    if r:
                        new_seed_ranges.append(r)
            #print()
        if not success:
            new_seed_ranges.append(s_r)
    new_seed_ranges=sorted(new_seed_ranges)
    #print("new: {}".format(new_seed_ranges))
    seed_ranges = new_seed_ranges
    #print()
print(new_seed_ranges[:1])
