INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

COUNT_2_RESULT = (
    "##..##..##..##..##..##..##..##..##..##..\n"
    "###...###...###...###...###...###...###.\n"
    "####....####....####....####....####....\n"
    "#####.....#####.....#####.....#####.....\n"
    "######......######......######......####\n"
    "#######.......#######.......#######....."
)
LINE_SIZE = 40
SCREEN_SIZE = 240

CODEPOINTS = [
    20, 60, 100, 140, 180, 220
]
INITIAL_VALUE = 1
NOOP = 'noop'
ADDX = 'addx'


def _prepare(line: str):
    return line.strip()


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def _get_score(data: list[int]) -> int:
    for point in CODEPOINTS:
        print(point * data[point])
    return sum([data[point - 1] * point for point in CODEPOINTS])


def _repeat_last(values_in_time: list[int]) -> None:
    values_in_time.append(_get_current_value(values_in_time))


def _get_current_value(values_in_time: list[int]) -> int:
    if not values_in_time:
        return INITIAL_VALUE
    return values_in_time[-1]


def _execute(data: list[str]) -> list[int]:
    values_in_time = [1]
    for cmd_line in data:
        if cmd_line.startswith(NOOP):
            _repeat_last(values_in_time)
        elif cmd_line.startswith(ADDX):
            _repeat_last(values_in_time)
            cmd_val = int(cmd_line.split()[1])

            values_in_time.append(cmd_val + _get_current_value(values_in_time))
    return values_in_time


def _format_screen(screen: str) -> str:
    splitted = []
    while chunk := screen[:LINE_SIZE]:
        splitted.append(f'{chunk}')
        screen = screen[LINE_SIZE:]
    return "\n".join(splitted)


def count(data: list[str]) -> int:
    values_in_time = _execute(data)
    return _get_score(values_in_time)


def count2(data: list[str]) -> str:
    screen = ""
    values_in_time = _execute(data)
    for pixel, value in enumerate(values_in_time[:SCREEN_SIZE]):
        char = '.'
        if (pixel % 40) in (value - 1, value, value + 1):
            char = '#'
        screen += char

    formatted = _format_screen(screen)
    # print(formatted)
    # print(COUNT_2_RESULT)
    return formatted


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    assert count(test_input_data) == 13140
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == COUNT_2_RESULT
    print(f"Part 2: \n{count2(get_data(INPUT_FILE))}")
