import utils

def parse_d2_game(line) -> (int, list):
    """
    input: "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    output: (4, [[' 1 green', ' 3 red', ' 6 blue'], [' 3 green', ' 6 red'], [' 3 green', ' 15 blue', ' 14 red\n']])
    """
    gameid_string, contents = line.split(":")
    gameid = int(utils.strip_non_numeric(gameid_string))
    games = [x.split(",") for x in contents.split(";")]
    return gameid, games

def get_colour_and_value(s) -> (str, int):
    """
    input: "12 green"
    output: ("green", 12)
    """
    colour = utils.strip_non_alpha(s)
    value = int(utils.strip_non_numeric(s))
    return colour, value

MAX_R = 12
MAX_G = 13
MAX_B = 14
with open("input/02/real.txt") as f:
    total = 0 # pt.1 answer
    power_sum = 0 # pt.2 answer
    for line in f:
        gameid, games = parse_d2_game(line)
        min_r = 0
        min_g = 0
        min_b = 0
        valid = True
        for game in games:
            r = 0
            g = 0
            b = 0
            for pick in game:
                colour, value = get_colour_and_value(pick)
                match colour:
                    case 'red':
                        min_r = max(value, min_r)
                        r += value
                    case 'green':
                        min_g = max(value, min_g)
                        g += value
                    case 'blue':
                        min_b = max(value, min_b)
                        b += value
                    case _:
                        raise("Unrecognised colour")
            if r > MAX_R or g > MAX_G or b > MAX_B:
                valid = False
        if valid:
            total += gameid
        power_sum += min_r * min_g * min_b

print(total)
print(power_sum)
