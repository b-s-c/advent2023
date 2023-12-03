import utils

# q2
total = 0
with open("input/01/real.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
        first_and_last = utils.get_first_and_last_int_occurrence(line)
        calibration = int("{}{}".format(first_and_last[0], first_and_last[1]))
        print(calibration)
        total += calibration
        print("Total: {}".format(total))
        print()


