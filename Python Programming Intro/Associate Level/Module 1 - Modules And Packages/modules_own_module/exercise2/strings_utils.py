import string_utils

def halve_strings(orig_strings):
    new_strings = []
    for el in orig_strings:
        new_strings.append(string_utils.halve_string(el))
    return new_strings