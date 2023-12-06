from math import prod

time_p1 = []
distance_p1 = []
time = 0
distance = 0

with open("input/06/real.txt") as f:
    for line in f:
        category, data = line.split(':')
        match category:
            case 'Time':
                time_p1 = list(map(int, data.split()))
                time = int("".join(data.split()))
            case 'Distance':
                distance_p1 = list(map(int, data.split()))
                distance = int("".join(data.split()))
            case _:
                raise("oops")

wins = [[] for _ in range(len(time_p1))]
for race in range(0, len(time_p1)):
    for hold_duration in range(0, time_p1[race]):
        time_to_move = time_p1[race] - hold_duration
        travel_distance = 0
        travel_distance = time_to_move * hold_duration
        if travel_distance > distance_p1[race]:
            #print("[race {}] hold duration: {}, travel distance: {}".format(race + 1, hold_duration, travel_distance))
            wins[race].append(hold_duration)

#print(wins)
p1_result = prod([len(x) for x in wins])
print(p1_result)

#print(time, distance)

lower_bound = 0
upper_bound = 0
for hold_duration in range(0, time):
    time_to_move = time - hold_duration
    travel_distance = time_to_move * hold_duration
    if travel_distance > distance:
        lower_bound = hold_duration
        break
for hold_duration in range(time, -1, -1):
    time_to_move = time - hold_duration
    travel_distance = time_to_move * hold_duration
    if travel_distance > distance:
        upper_bound = hold_duration
        break
#print(lower_bound, upper_bound)
print(upper_bound - lower_bound + 1) # p2
