def day_6_1():
    with open("data/input6.txt") as file:
        x = file.read()

    for y in range(0, len(x) - 3):
        char_set = x[y : y + 4]
        if len(set(char_set)) == 4:
            return y + 4


def day_6_2():
    with open("data/input6.txt") as file:
        x = file.read()

    for y in range(0, len(x) - 13):
        char_set = x[y : y + 14]
        if len(set(char_set)) == 14:
            return y + 14
