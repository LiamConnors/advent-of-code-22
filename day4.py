def day_4_1():
    with open("data/input4.txt") as file:
        x = file.read()
    newlist = []
    for y in x.split():
        newlist.append(y.split(","))

    complete_overlaps = 0
    for group in newlist:
        list_1 = list(
            range(int(group[0].split("-")[0]), int(group[0].split("-")[1]) + 1)
        )
        list_2 = list(
            range(int(group[1].split("-")[0]), int(group[1].split("-")[1]) + 1)
        )
        if all(item in list_1 for item in list_2):
            complete_overlaps += 1
        elif all(item in list_2 for item in list_1):
            complete_overlaps += 1
    return complete_overlaps


def day_4_2():
    with open("data/input4.txt") as file:
        x = file.read()
    newlist = []
    for y in x.split():
        newlist.append(y.split(","))

    complete_overlaps = 0
    for group in newlist:
        list_1 = list(
            range(int(group[0].split("-")[0]), int(group[0].split("-")[1]) + 1)
        )
        list_2 = list(
            range(int(group[1].split("-")[0]), int(group[1].split("-")[1]) + 1)
        )
        if any(item in list_1 for item in list_2):
            complete_overlaps += 1
        elif any(item in list_2 for item in list_1):
            complete_overlaps += 1
    return complete_overlaps
