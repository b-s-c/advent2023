import utils

def q1():
    with open("input/02/real.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            print(line)
            gameid, games = utils.parse_d2_game(line)
            MAX_R = 12
            MAX_G = 13
            MAX_B = 14
            valid = True
            for game in games:
                r = 0
                g = 0
                b = 0
                for pick in game:
                    colour, value = utils.get_colour_and_value(pick)
                    match colour:
                        case 'red':
                            r += value
                        case 'green':
                            g += value
                        case 'blue':
                            b += value
                        case _:
                            raise("Unrecognised colour")
                print(r, g, b)
                if r > MAX_R or g > MAX_G or b > MAX_B:
                    valid = False
                    break
            if valid:
                total += gameid
            print(total)

def q2():
    with open("input/02/real.txt") as f:
        power_sum = 0
        for line in f:
            #line = line.strip()
            #print(line)

            #print(utils.parse_d2_game(line))
            _, games = utils.parse_d2_game(line)

            min_r = 0
            min_g = 0
            min_b = 0

            for game in games:
                for pick in game:
                    colour, value = utils.get_colour_and_value(pick)
                    match colour:
                        case 'red':
                            min_r = max(value, min_r)
                        case 'green':
                            min_g = max(value, min_g)
                        case 'blue':
                            min_b = max(value, min_b)
                        case _:
                            raise("Unrecognised colour")
            #print(min_r, min_g, min_b)
            power = min_r * min_g * min_b
            #print(power)
            power_sum += power
        print(power_sum)

q2()
