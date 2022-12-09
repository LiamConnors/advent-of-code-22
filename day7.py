from pathlib import Path
import pandas as pd


def day_7_1():

    with open("data/input7.txt") as file:
        x = file.read()

    input = x.splitlines()

    directory_structure = {"/": 0}
    file_sizes = {}
    directory_sizes = {}

    # Track current directory
    cwd = Path()

    # Generate directory structure and get list of files and sizes
    for line in input:
        command_start = line.split()[0]

        if command_start == "$":
            command_type = line.split()[1]
            if command_type == "cd":
                directory = line.split()[2]
                if directory == "..":
                    cwd = cwd.parent
                elif directory == "/":
                    cwd = Path("/")
                else:
                    cwd = cwd / directory

        elif command_start == "dir":
            directory_name = cwd / line.split()[1]
            directory_structure[str(directory_name)] = 0
        else:
            file_path = cwd / line.split()[1]
            file_sizes[str(file_path)] = line.split()[0]

    # Calculate directory sizes
    for dir_name, val in directory_structure.items():
        total = 0
        for file, val2 in file_sizes.items():
            directory_length = len(dir_name)
            if len(file) >= directory_length:
                if dir_name in file[:directory_length]:
                    total += int(val2)
                else:
                    continue
        directory_sizes[dir_name] = total

    df = pd.DataFrame(list(directory_sizes.items()), columns=["Directory", "Size"])
    return df[df.Size <= 100000]["Size"].sum()


def day_7_2():

    with open("data/input7.txt") as file:
        x = file.read()

    input = x.splitlines()

    directory_structure = {"/": 0}
    file_sizes = {}
    directory_sizes = {}

    # Track current directory
    cwd = Path()

    # Generate directory structure and get list of files and sizes
    for line in input:
        command_start = line.split()[0]

        if command_start == "$":
            command_type = line.split()[1]
            if command_type == "cd":
                directory = line.split()[2]
                if directory == "..":
                    cwd = cwd.parent
                elif directory == "/":
                    cwd = Path("/")
                else:
                    cwd = cwd / directory

        elif command_start == "dir":
            directory_name = cwd / line.split()[1]
            directory_structure[str(directory_name)] = 0
        else:
            file_path = cwd / line.split()[1]
            file_sizes[str(file_path)] = line.split()[0]

    # Calculate directory sizes
    for dir_name, val in directory_structure.items():
        total = 0
        for file, val2 in file_sizes.items():
            directory_length = len(dir_name)
            if len(file) >= directory_length:
                if dir_name in file[:directory_length]:
                    total += int(val2)
                else:
                    continue
        directory_sizes[dir_name] = total

    total_storage_capacity = 70000000
    free_space = total_storage_capacity - directory_sizes["/"]
    required_space = 30000000 - free_space

    df = pd.DataFrame(list(directory_sizes.items()), columns=["Directory", "Size"])
    directory_to_del_size = (
        df[df.Size >= required_space]
        .sort_values(by=["Size"])["Size"]
        .iloc[:1]
        .to_string(index=False)
    )

    return int(directory_to_del_size)
