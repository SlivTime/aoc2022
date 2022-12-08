INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

def _prepare(line: str) -> tuple[list[int], list[int]]:
    a, b, c, d = [int(x) for x in line.replace(',', '-').split('-')]
    return list(range(a, b+1)), list(range(c, d+1))


def get_data(filename: str) -> list[tuple[str, str]]:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def count(data: list[tuple[list[int], list[int]]]) -> int:
    result = 0
    for row in data:
        s1, s2 = set(row[0]), set(row[1])
        if s1.issubset(s2) or s2.issubset(s1):
            result += 1
    return result


def count2(data: list[tuple[list[int], list[int]]]) -> int:
    result = 0
    for row in data:
        s1, s2 = set(row[0]), set(row[1])
        if s1.intersection(s2):
            result += 1
    return result


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data) == 2
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 4
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
