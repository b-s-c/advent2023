with open("input/15/real.txt") as f:
    steps = f.read().strip().split(',')
print(steps)

def hash_algorithm(s) -> int:
    current_value = 0
    for code in map(ord, s):
        current_value = ((current_value + code) * 17) % 256
    return current_value

#print(hash_algorithm('HASH'))
total = 0
for step in steps:
    #print(hash_algorithm(step))
    total += hash_algorithm(step)
print(f'p1: {total}')

def decision(s) -> (str, str, int):
    if '=' in s:
        operation = 'set'
        label, value = s.split('=')
        return operation, label, value
    elif '-' in s:
        operation = 'rem'
        label = s.split('-')[0]
        return operation, label, None
    return False

boxes = {i:[] for i in range(256)}
def box_set(label, value):
    contents = boxes[hash_algorithm(label)]
    for i, item in enumerate(contents):
        if item[0] == label:
            contents[i] = (label, value)
            return
    contents.append((label, value))

def box_rem(label):
    contents = boxes[hash_algorithm(label)]
    for i, item in enumerate(contents):
        if item[0] == label:
            del(contents[i])
            return True
    return False

def print_boxes():
    for key, value in boxes.items():
        if value:
            print(key, value)

#for step in steps: print(step, decision(step))

for step in steps:
    operation, label, value = decision(step)
    match operation:
        case 'set':
            box_set(label, value)
        case 'rem':
            box_rem(label)
print_boxes()

total_p2 = 0
for key, value in boxes.items():
    if value:
        for i, value in enumerate(value):
            box_num = key + 1
            slot = i + 1
            focal_length = int(value[1])
            total_p2 += box_num * slot * focal_length

print(total_p2)
