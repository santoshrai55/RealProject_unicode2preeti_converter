import re
from . import custom_data
custom_data_source = custom_data.custom_data_source
custom_data_target = custom_data.custom_data_target


def converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    result = regex.sub(lambda match: substitutions[match.group(0)], string)
    n = 0

    while len(custom_data_source) < 7:
        result = result.replace(custom_data_source[n], custom_data_target[n])
        n += 1
    return result
