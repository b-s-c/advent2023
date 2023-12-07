from functools import cmp_to_key
from operator import itemgetter

hands = []
bets = []
#card_hierarchy = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] # p1 card hierarchy
card_hierarchy = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_value_dict = {card:card_hierarchy.index(card) for card in card_hierarchy}

with open("input/07/big.txt") as f:
    for line in f:
        hand, bet = line.split()
        hands.append(hand)
        bets.append(int(bet))

def get_hand_type(hand: str) -> int:
    """
    0: five of a kind  (AAAAA)
    1: four of a kind  (AAAAB)
    2: full house      (ABABA)
    3: three of a kind (AAABC)
    4: two pair        (22334)
    5: one pair        (22345)
    6: high card       (23456)
    """
    symbol_dict = {symbol:hand.count(symbol) for symbol in hand if symbol != 'J'}
    if not symbol_dict:
        return 0 # five of a kind on 'J'
    if 'J' in hand:
        symbol_dict[max(symbol_dict.items(), key=itemgetter(1))[0]] += list(hand).count('J')
    counts = symbol_dict.values()
    if 5 in counts:
        return 0 # five of a kind (again)
    if 4 in counts:
        return 1 # four of a kind
    if 3 in counts:
        if 2 in counts:
            return 2 # full house
        return 3 # three of a kind
    if 2 in counts:
        if list(counts).count(2) == 2:
            return 4 # two pair
        return 5 # one pair
    return 6 # high card

def compare_two_hands(hand_1: tuple, hand_2: tuple) -> str:
    for i in range(0, len(hand_1[0])):
        hand_1_card_value = card_value_dict[hand_1[0][i]]
        hand_2_card_value = card_value_dict[hand_2[0][i]]
        if hand_1_card_value < hand_2_card_value:
            return -1
        if hand_2_card_value < hand_1_card_value:
            return 1
    return 0 # hands are equal
    
hand_type_counts = [[] for _ in range(7)]
for i, hand in enumerate(hands):
    hand_type_counts[get_hand_type(hand)].append((hand, bets[i]))

rank = len(hands)
total_winnings = 0
for i in range(len(hand_type_counts)):
    #print("\nCategory {}".format(i))
    hands = hand_type_counts[i]
    for hand in sorted(hands, key=cmp_to_key(compare_two_hands)):
        total_winnings += rank * hand[1]
        #print("hand: {}, bet: {}".format(*hand))
        #print("added {}*{}={}".format(rank, hand[1], rank*hand[1]))
        rank -= 1
print(total_winnings)
