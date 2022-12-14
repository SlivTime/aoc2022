import re
from collections import defaultdict

INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

cd_re = re.compile(r"\$ cd (.*)")
ls_re = re.compile(r"\$ ls")


def _prepare(line: str):
    return line


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def count_filtered_sum(sizes: dict[str, int], border: int) -> int:

    return sum([size for size in sizes.values() if size < border])


def _joinpath(path: list[str]) -> str:
    joined = "/".join(path[1:])
    return f"/{joined}"


def _get_sizes(data: list[str]) -> dict[str, int]:
    sizes = defaultdict(int)
    path = []
    for line in data:
        if curdirs := cd_re.findall(line):
            dest = curdirs[0]
            if dest == "..":
                path.pop()
            else:
                sizes.setdefault(dest, 0)
                path.append(dest)
        elif ls_re.match(line):
            ...
        else:
            fsize, _ = line.split()
            if fsize.isdigit():
                for i in range(len(path)):
                    dirpath = _joinpath(path[: i + 1])
                    sizes[dirpath] += int(fsize)
    return sizes


def count(data: list[str]) -> int:
    sizes = _get_sizes(data)

    return count_filtered_sum(sizes, 100_000)


def count2(data: list[str]) -> int:
    sizes = _get_sizes(data)
    total = 70_000_000
    need = 30_000_000
    now_taken = sizes["/"]
    need_free = total - need

    for sz in sorted(sizes.values()):
        if (now_taken - sz) < need_free:
            return sz
    return 0


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    assert count(test_input_data) == 95437
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 24933642
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
