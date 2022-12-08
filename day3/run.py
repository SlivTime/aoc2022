from string import ascii_letters

INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"


def get_data(filename: str) -> list[tuple[str, str]]:
    with open(filename) as f:
        return [x.strip() for x in f]


def _score(char: str) -> int:
    return ascii_letters.index(char) + 1

def count(data: list[str]) -> int:
    result = 0
    for row in data:
        half = int(len(row) / 2)
        left, right = row[:half], row[half:]
        print(left, right)
        both = set(left).intersection(set(right))
        print(both)
        for ch in both:
            result += _score(ch)
        print(result)
    return result


def count2(data: list[tuple[str, str]]) -> int:
    result = 0
    while True:
        batch = data[:3]
        print(batch)
        if not batch:
            break
        a, b, c = batch
        common = set(a).intersection(set(b))
        common = set(common).intersection(set(c))
        for ch in common:
            print(ch)
            result += _score(ch)
        data = data[3:]
        print(result)
    return result


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data) == 157
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 70
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
