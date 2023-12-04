import utils
from math import pow

def get_winnings(num_wins: int) -> int:
    if num_wins == 0: return 0
    return int(pow(2, num_wins - 1))
def play_card(calls: set, picks: set) -> int:
    return len(calls.intersection(picks))

wins = []
with open("input/04/real.txt") as f:
    for line in f:
        _, game = line.strip().split(":")
        calls, picks = (set(y) for y in ((x.split()) for x in game.split(" | ")))
        wins.append(play_card(calls, picks))

p2_copies_dict = {}
for card in range(0, len(wins)):
    utils.dict_increment(p2_copies_dict, card, 1)
    for new_card in range(card + 1, card + 1 + wins[card]):
        utils.dict_increment(p2_copies_dict, new_card, p2_copies_dict[card])

p1_total = sum(list(map(get_winnings, wins)))
print(p1_total)
print(sum(p2_copies_dict.values()))
