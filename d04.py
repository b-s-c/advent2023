from math import pow
def get_winnings(num_wins: int) -> int:
    """
    0, 1, 2, 4, 8, 16, 32, ...
    """
    if num_wins == 0: return 0
    return int(pow(2, num_wins - 1))
def play_card(calls, picks) -> int:
    matches = 0
    for call in calls:
        if call in picks:
            matches += 1
    return matches

win_values = {}
wins = []
#cards = []
with open("input/04/real.txt") as f:
    for card_id, line in enumerate(f):
        matches = 0
        gameid, game = line.strip().split(":")
        calls, picks = (set(map(int, y)) for y in ((x.strip().split()) for x in game.split(" | ")))
        wins.append(play_card(calls, picks))
        win_values[card_id] = play_card(calls, picks)

p1_total = list(map(get_winnings, wins))
print(sum(p1_total))

p2_total = len(win_values)
cards_to_check = list(range(0, p2_total))
while cards_to_check:
    card_id = cards_to_check.pop(0)
    more_cards = win_values[card_id]
    for new_card_id in range(card_id+1, card_id+1+more_cards):
        cards_to_check.append(new_card_id)
        p2_total += 1
print(p2_total)
