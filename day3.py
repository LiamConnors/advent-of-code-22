import string


def day_3_1():
    with open("data/input3.txt") as file:
        x = file.read()
    data = x.split()

    letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priority_mapping = {}
    for index, letter in enumerate(letters_list):
        priority_mapping[letter] = index + 1

    total = 0
    for rucksack in data:
        first = rucksack[: len(rucksack) // 2]
        second = rucksack[len(rucksack) // 2 :]
        common = list(set(first) & set(second))
        total += priority_mapping[common[0]]
    return total


def day_3_2():
    with open("data/input3.txt") as file:
        x = file.read()
    data = x.split()

    letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priority_mapping = {}
    for index, letter in enumerate(letters_list):
        priority_mapping[letter] = index + 1

    elf_groups = []
    e = 0
    for v in range(0, len(data) // 3):
        elf_groups.append(data[e : e + 3])
        common = list(
            set(data[e : e + 3][0]) & set(data[e : e + 3][1]) & set(data[e : e + 3])
        )
        e += 3

    total = 0
    for e in elf_groups:
        common = list(set.intersection(*map(set, e)))
        total += priority_mapping[common[0]]
    return total
