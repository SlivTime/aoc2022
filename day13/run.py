import json
from functools import cmp_to_key
from itertools import zip_longest

import more_itertools

INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"


def _prepare(lines: tuple[str, str, str]) -> tuple[list, list]:
    left_str = more_itertools.first(lines)
    right_str = more_itertools.nth(lines, 1)
    return json.loads(left_str), json.loads(right_str)


def get_data(filename: str) -> list[tuple[str, str]]:
    data = []
    with open(filename) as f:
        for chunk in more_itertools.chunked(f, 3):
            data.append(_prepare(chunk))
    return data


def cmp(left, right) -> int:
    match left, right:
        case int(), int():
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0
        case list(), list():
            for r in [cmp(l, r) for l, r in zip_longest(left, right)]:
                if r != 0:
                    return r
            return cmp(len(left), len(right))
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case None, _:
            return -1
        case _, None:
            return 1
        case _:
            raise ValueError(f"Unknown type: {left}, {right}")


def count(data: list[tuple[str, str]]) -> int:
    in_order = []
    for idx, (left, right) in enumerate(data, start=1):
        if r := cmp(left, right) <= 0:
            in_order.append(idx)

    return sum(in_order)


def count2(data: list[tuple[str, str]]) -> int:
    result = 0
    div1 = [[2]]
    div2 = [[6]]
    flat = list(more_itertools.flatten(data)) + [div1, div2]
    flat.sort(key=cmp_to_key(cmp))
    pos1 = flat.index(div1) + 1
    pos2 = flat.index(div2) + 1
    return pos1 * pos2


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data) == 13
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 140
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
