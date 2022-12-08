INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"


def _prepare(line: str):
    return line


def get_data(filename: str) -> str:
    with open(filename) as f:
        return f.read().strip()


def count(data: str, unique_count) -> int:
    for idx in range(len(data)):
        slice = data[idx - unique_count : idx]
        if len(set(slice)) == unique_count:
            return idx


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data, 4) == 11
    print(f"Part 1: {count(get_data(INPUT_FILE), 4)}")
    assert count(test_input_data, 14) == 26
    print(f"Part 2: {count(get_data(INPUT_FILE), 14)}")
