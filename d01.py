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

def get_first_and_last_values(s: str, things_to_find: list) -> (str, str):
    min_index = len(s)
    max_index = -1
    min_value = -1
    max_value = -1
    for search_value in things_to_find:
        low_index = s.find(search_value)
        if low_index == -1: # not found
            continue
        high_index = s.rfind(search_value)
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

total_p1 = 0
total_p2 = 0
p1_things_to_find = list(string_to_intstring.values())
p2_things_to_find = p1_things_to_find + list(string_to_intstring.keys())
with open("input/01/real.txt") as f:
    for line in f:
        line = line.strip()
        first_and_last_p1 = get_first_and_last_values(line, p1_things_to_find)
        first_and_last_p2 = get_first_and_last_values(line, p2_things_to_find)
        total_p1 += int("{}{}".format(*first_and_last_p1))
        total_p2 += int("{}{}".format(*first_and_last_p2))
print(total_p1)
print(total_p2)
