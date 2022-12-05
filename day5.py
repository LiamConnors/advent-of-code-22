from collections import deque


def day_5_1():
    with open("data/input5.txt") as file:
        x = file.read()

    data = x.splitlines()

    queues_num = data[8].split()

    dict_of_queues = {}
    positions_in_row = {}

    for n in queues_num:
        dict_of_queues[n] = deque()

    position_of_value = 1
    for n in queues_num:
        positions_in_row[n] = position_of_value
        position_of_value += 4

    crate_rows = data[0:8]

    crate_rows.reverse()

    for row in crate_rows:
        for q, pos in positions_in_row.items():
            if row[pos] == " ":
                continue
            else:
                dict_of_queues[q].appendleft(row[pos])

    moves = data[10:]

    list_of_moves = []

    for m in moves:
        list_of_moves.append(
            {
                "moves": m.lstrip("move ").split(" from ")[0],
                "from": m.lstrip("move ").split(" from ")[1].split(" to ")[0],
                "to": m.lstrip("move ").split(" from ")[1].split(" to ")[1],
            }
        )

    for move in list_of_moves:
        for number in range(0, int(move["moves"])):
            x = dict_of_queues[move["from"]].popleft()
            dict_of_queues[move["to"]].appendleft(x)

    message = ""
    for k, d in enumerate(dict_of_queues):
        message += dict_of_queues[d][0]
    return message


def day_5_2():
    with open("data/input5.txt") as file:
        x = file.read()

    data = x.splitlines()

    queues_num = data[8].split()

    dict_of_queues = {}
    positions_in_row = {}

    for n in queues_num:
        dict_of_queues[n] = deque()

    position_of_value = 1
    for n in queues_num:
        positions_in_row[n] = position_of_value
        position_of_value += 4

    crate_rows = data[0:8]

    crate_rows.reverse()

    for row in crate_rows:
        for q, pos in positions_in_row.items():
            if row[pos] == " ":
                continue
            else:
                dict_of_queues[q].appendleft(row[pos])

    moves = data[10:]

    list_of_moves = []

    for m in moves:
        list_of_moves.append(
            {
                "moves": m.lstrip("move ").split(" from ")[0],
                "from": m.lstrip("move ").split(" from ")[1].split(" to ")[0],
                "to": m.lstrip("move ").split(" from ")[1].split(" to ")[1],
            }
        )

    for move in list_of_moves:
        reversed_list = []
        for val in range(0, int(move["moves"])):
            x = dict_of_queues[move["from"]].popleft()
            reversed_list.append(x)
        reversed_list.reverse()
        dict_of_queues[move["to"]].extendleft(reversed_list)

    message = ""
    for k, d in enumerate(dict_of_queues):
        message += dict_of_queues[d][0]
    return message
