import math

def halve_string(orig_string):
    midpoint = math.ceil(len(orig_string) / 2)
    return orig_string[:midpoint], orig_string[midpoint:]