import re

def strip_non_numeric(s) -> str:
    return ''.join([i for i in s if i.isdigit()])
def strip_non_alpha(s) -> str:
    return ''.join([i for i in s if i.isalpha()])
def dict_increment(d: dict, k, inc=1):
    if k in d:
        d[k] += inc
    else:
        d[k] = inc
