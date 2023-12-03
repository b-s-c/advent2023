import re

string_to_intstring = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
master_string_list = list(string_to_intstring.keys()) + list(string_to_intstring.values())

def strip_non_numeric(s) -> str:
    return ''.join([i for i in s if i.isdigit()])
def strip_non_alpha(s) -> str:
    return ''.join([i for i in s if i.isalpha()])

def get_first_and_last_int_occurrence(s) -> (str, str):
    min_index = len(s)
    max_index = -1
    min_value = -1
    max_value = -1
    for search_value in master_string_list:
        low_index = s.find(search_value)
        high_index = s.rfind(search_value)
        if low_index == -1 or high_index == -1: # shouldn't actually ever hit the second clause
            continue
        if low_index < min_index:
            min_index = low_index
            min_value = search_value
        if high_index > max_index:
            max_index = high_index
            max_value = search_value
    if min_value in string_to_intstring:
        min_value = string_to_intstring[min_value]
    if max_value in string_to_intstring:
        max_value = string_to_intstring[max_value]
    return min_value, max_value

def parse_d2_game(line) -> (int, list):
    """
    input: "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    output: (4, [[' 1 green', ' 3 red', ' 6 blue'], [' 3 green', ' 6 red'], [' 3 green', ' 15 blue', ' 14 red\n']])
    """
    gameid_string, contents = line.split(":")
    gameid = int(strip_non_numeric(gameid_string))
    games = [x.split(",") for x in contents.split(";")]
    return gameid, games

def get_colour_and_value(s) -> (str, int):
    """
    input: "12 green"
    output: ("green", 12)
    """
    colour = strip_non_alpha(s)
    value = int(strip_non_numeric(s))
    return colour, value

def is_symbol_d3(s: str) -> bool:
    if s.isdigit(): return False
    if s == '.': return False
    return True

def dict_increment(d: dict, k, inc=1):
    if k in d:
        d[k] += inc
    else:
        d[k] = inc
