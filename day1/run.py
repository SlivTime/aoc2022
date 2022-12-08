INPUT_FILE = "input.txt"

def get_data():
    # return TEST_DATA
    with open(INPUT_FILE) as f:
        data = [x for x in f]
    return data

def extract_sums(data: list[str]) -> list[int]:
    cur = 0
    res = []
    for item in data:
        try:
            cur += int(item)
        except ValueError:
            res.append(cur)
            cur = 0
    return res

def count(data: list[str]) -> int:
    sums = extract_sums(data)
    return max(sums)

def count2(data: list[str]) -> int:
    sums = sorted(extract_sums(data))
    return sum(sums[-3:])

if __name__ == "__main__":
    input_data = get_data()
    print(f"Part 1: {count(input_data)}")
    print(f"Part 1: {count2(input_data)}")
