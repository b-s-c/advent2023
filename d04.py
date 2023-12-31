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
        wins.append(play_card(*(set(y) for y in ((x.split()) for x in line.strip().split(':')[1].split(" | ")))))

p2_card_count = {}
for card in range(0, len(wins)):
    utils.dict_increment(p2_card_count, card, 1)
    for new_card in range(card + 1, card + 1 + wins[card]):
        utils.dict_increment(p2_card_count, new_card, p2_card_count[card])

print(sum(map(get_winnings, wins))) # part 1
print(sum(p2_card_count.values())) # part 2
