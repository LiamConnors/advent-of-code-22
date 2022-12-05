def day_2_1():
    with open("data/input2.txt") as file:
        x = file.read()
    hands = [y.split(" ") for y in x.split("\n")]
    total_score = 0
    for hand in hands:
        if hand[0] == "A" and hand[1] == "X":
            total_score += 4
        if hand[0] == "A" and hand[1] == "Y":
            total_score += 8
        if hand[0] == "A" and hand[1] == "Z":
            total_score += 3
        if hand[0] == "B" and hand[1] == "X":
            total_score += 1
        if hand[0] == "B" and hand[1] == "Y":
            total_score += 5
        if hand[0] == "B" and hand[1] == "Z":
            total_score += 9
        if hand[0] == "C" and hand[1] == "X":
            total_score += 7
        if hand[0] == "C" and hand[1] == "Y":
            total_score += 2
        if hand[0] == "C" and hand[1] == "Z":
            total_score += 6
    return total_score


def day_2_2():
    with open("data/input2.txt") as file:
        x = file.read()
    hands = [y.split(" ") for y in x.split("\n")]
    new_list = []
    for hand in hands:
        if hand[0] == "A" and hand[1] == "X":
            new_list.append(["A", "Z"])
        if hand[0] == "A" and hand[1] == "Y":
            new_list.append(["A", "X"])
        if hand[0] == "A" and hand[1] == "Z":
            new_list.append(["A", "Y"])
        if hand[0] == "B" and hand[1] == "X":
            new_list.append(["B", "X"])
        if hand[0] == "B" and hand[1] == "Y":
            new_list.append(["B", "Y"])
        if hand[0] == "B" and hand[1] == "Z":
            new_list.append(["B", "Z"])
        if hand[0] == "C" and hand[1] == "X":
            new_list.append(["C", "Y"])
        if hand[0] == "C" and hand[1] == "Y":
            new_list.append(["C", "Z"])
        if hand[0] == "C" and hand[1] == "Z":
            new_list.append(["C", "X"])
    total_score = 0
    for hand in new_list:
        if hand[0] == "A" and hand[1] == "X":
            total_score += 4
        if hand[0] == "A" and hand[1] == "Y":
            total_score += 8
        if hand[0] == "A" and hand[1] == "Z":
            total_score += 3
        if hand[0] == "B" and hand[1] == "X":
            total_score += 1
        if hand[0] == "B" and hand[1] == "Y":
            total_score += 5
        if hand[0] == "B" and hand[1] == "Z":
            total_score += 9
        if hand[0] == "C" and hand[1] == "X":
            total_score += 7
        if hand[0] == "C" and hand[1] == "Y":
            total_score += 2
        if hand[0] == "C" and hand[1] == "Z":
            total_score += 6
    return total_score
