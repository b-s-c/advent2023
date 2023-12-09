with open("input/09/big.txt") as f:
    input = [list(map(int, line.strip().split())) for line in f.readlines()]

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

def extrapolate(seqs: list[list[int]]) -> list[list[int]]:
    seqs[-1].extend([0, 0])
    for seq_i in range(len(seqs) - 2, -1, -1):
        seq = seqs[seq_i]
        seq.append(seq[-1] + seqs[seq_i + 1][-1])
        seq.insert(0, seq[0] - seqs[seq_i + 1][0])
    return seqs

full_sequences = []
for line in input:
    current_result = [line]
    diff = line
    while not is_all_zero(diff):
        diff = get_sequence_difference(diff)
        current_result.append(diff)
    full_sequences.append(current_result)

p1_total = 0
p2_total = 0
for extrapolated_top_line in [extrapolate(fs)[0] for fs in full_sequences]:
    p1_total += extrapolated_top_line[-1]
    p2_total += extrapolated_top_line[0]

print(p1_total)
print(p2_total)
