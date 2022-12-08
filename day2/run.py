INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'
OP_ROCK = 'A'
OP_PAPER = 'B'
OP_SCISSORS = 'C'

def get_data(filename: str) -> list[tuple[str, str]]:
    # return TEST_DATA
    with open(filename) as f:
        data = [x.split() for x in f]
    return data

def choice_score(choice: str):
    scores = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }
    return scores[choice]

def round_score(op: str, my: str) -> int:
    scores = {
        (OP_ROCK, ROCK): 3,
        (OP_PAPER, PAPER): 3,
        (OP_SCISSORS, SCISSORS): 3,
        (OP_SCISSORS, ROCK): 6,
        (OP_ROCK, PAPER): 6,
        (OP_PAPER, SCISSORS): 6,
    }
    return scores.get((op, my), 0)

def calculate_score(op: str, my: str) -> int:
    return choice_score(my) + round_score(op, my)

def count(data: list[tuple[str, str]]) -> int:
    scores = [calculate_score(*round) for round in data]
    return sum(scores)

def chose_choice(op: str, result: str) -> str:
    result_map = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    need_result = result_map[result]
    for my_choice in (ROCK, PAPER, SCISSORS):
        score = round_score(op, my_choice)
        if score == need_result:
            return my_choice

def count2(data: list[tuple[str, str]]) -> int:
    result = 0
    
    for round in data:
        op, my_result = round
        my_choice = chose_choice(op, my_result)
        result += calculate_score(op, my_choice)
    return result

if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data) == 15
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 12
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
