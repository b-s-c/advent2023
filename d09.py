with open("input/09/real.txt") as f:
    input = [list(map(int, line.strip().split())) for line in f.readlines()]

print(input)

def is_all_zero(seq: list[int]) -> bool:
    for item in seq:
        if item != 0:
            return False
    return True

def get_sequence_difference(seq: list[int]) -> list[int]:
    """
    in:  [3, 6, 9, 12]
    out: [0, 3, 3, 3]
    """
    out = []
    for i in range(1, len(seq)):
        out.append(seq[i] - seq[i - 1])
    return out

def extrapolate_forwards(seqs: list[list[int]]) -> list[list[int]]:
    zeros = seqs[-1]
    seqs[-1].append(0)
    for seq_i in range(len(seqs) - 2, -1, -1):
        seq = seqs[seq_i]
        value = seq[-1] + seqs[seq_i + 1][-1]
        seq.append(value)
    return seqs

def extrapolate_backwards(seqs: list[list[int]]) -> list[list[int]]:
    zeros = seqs[-1]
    seqs[-1].insert(0, 0)
    for seq_i in range(len(seqs) - 2, -1, -1):
        seq = seqs[seq_i]
        value = seq[0] - seqs[seq_i + 1][0]
        seq.insert(0, value)
    return seqs

result = []
for line in input:
    current_result = [line]
    diff = line
    while not is_all_zero(diff):
        diff = get_sequence_difference(diff)
        current_result.append(diff)
    result.append(current_result)

p1_total = 0
p2_total = 0
for i in range(0, len(result)):
    result[i] = extrapolate_forwards(result[i])
    p1_total += result[i][0][-1]
    result[i] = extrapolate_backwards(result[i])
    p2_total += result[i][0][0]
print(p1_total)
print(p2_total)
