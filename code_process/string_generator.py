import random
import string


def create_strings_from_file(filename, count):
    """
        Create all strings by reading lines in specified files
    """
    strings = []
    with open(filename, 'r', encoding="utf8") as f:
        lines = [l.strip()[0:200] for l in f.readlines()]
        if len(lines) == 0:
            raise Exception("No lines could be read in file")
        while len(strings) < count:
            if len(lines) >= count - len(strings):
                strings.extend(lines[0:count - len(strings)])
            else:
                strings.extend(lines)
    return strings


def select_string_from_file(filename):
    """
        Select a string by randomint()
    """
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise Exception("No lines could be read in file")
        line = random.sample(lines, 1)[0]
    return line


def select_strings_from_file(filename,num):
    """
        Select a string by randomint()
    """
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise Exception("No lines could be read in file")
        result = ""
        for _ in range(num):
            result = result + random.sample(lines, 1)[0]
        print(result)
    return result


def create_strings_randomly(length, allow_variable, count, let, num, sym, lang):
    """
        Create all strings by randomly sampling from a pool of characters.
    """
    # If none specified, use all three
    if True not in (let, num, sym):
        let, num, sym = True, True, True
    pool = ''
    if let:
        if lang == 'cn':
            pool += ''.join([chr(i) for i in range(19968, 40908)])  # Unicode range of CHK characters
        else:
            pool += string.ascii_letters
    if num:
        pool += "0123456789"
    if sym:
        pool += "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"

    if lang == 'cn':
        min_seq_len = 1
        max_seq_len = 2
    else:
        min_seq_len = 2
        max_seq_len = 10
    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, random.randint(1, length) if allow_variable else length):
            seq_len = random.randint(min_seq_len, max_seq_len)
            current_string += ''.join([random.choice(pool) for _ in range(seq_len)])
            current_string += ' '
        strings.append(current_string[:-1])
    return strings