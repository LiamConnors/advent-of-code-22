def day_1_1():
    with open("data/input1.txt") as file:
        x = file.read()
    _elves = x.split("\n\n")
    elves = []
    for x in _elves:
        y = x.split("\n")
        elves.append(y)

    summed_values = []
    for elf in elves:
        elf = list(filter(None, elf))
        summed_values.append(sum(list(map(int, elf))))

    summed_values.sort(reverse=True)
    return summed_values[0]


def day_1_2():
    with open("data/input1.txt") as file:
        x = file.read()
    _elves = x.split("\n\n")
    elves = []
    for x in _elves:
        y = x.split("\n")
        elves.append(y)

    summed_values = []
    for elf in elves:
        elf = list(filter(None, elf))
        summed_values.append(sum(list(map(int, elf))))

    summed_values.sort(reverse=True)
    return sum(summed_values[:3])
