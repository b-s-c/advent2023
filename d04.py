from math import pow
def get_winnings(num_wins: int) -> int:
    """
    0, 1, 2, 4, 8, 16, 32
    """
    if num_wins == 0: return 0
    return int(pow(2, num_wins - 1))

wins = []
with open("input/04/real.txt") as f:
    for line in f:
        matches = 0
        gameid, game = line.split(":")
        calls, picks = (set(map(int, y)) for y in ((x.strip().split()) for x in game.split(" | ")))
        print(calls)
        print(picks)
        for call in calls:
            if call in picks:
                matches += 1
        wins.append(matches)

p1_total = list(map(get_winnings, wins))
print(sum(p1_total))
