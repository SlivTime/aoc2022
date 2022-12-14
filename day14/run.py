INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

Point = tuple[int, int]

SOURCE = (500, 0)


class ToTheMoon(Exception):
    ...


def get_data(filename: str) -> set[Point]:
    shape = set()
    with open(filename) as f:
        for line in f:
            splitted = line.strip().split(" -> ")
            for from_, to_ in zip(splitted, splitted[1:]):
                x1, y1 = map(int, from_.split(","))
                x2, y2 = map(int, to_.split(","))
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        shape.add((x, y))
    return shape


def _is_standing_still(shape: set[Point], point: Point) -> bool:
    # 3 dots must be at bottom
    x, y = point
    floor = {(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)}
    return floor.issubset(shape)


def _is_gone_forever(point: Point, floor_level: int) -> bool:
    return point[1] > floor_level


def _can_fall_down(shape: set[Point], point: Point) -> bool:
    x, y = point
    return (x, y + 1) not in shape


def _can_fall_left(shape: set[Point], point: Point) -> bool:
    x, y = point
    return (x - 1, y + 1) not in shape


def _can_fall_right(shape: set[Point], point: Point) -> bool:
    x, y = point
    return (x + 1, y + 1) not in shape


def _try_to_fall(shape: set[Point], point: Point, platform_level: int) -> int:
    while True:
        if _is_gone_forever(point, platform_level):
            raise ToTheMoon()
        elif _is_standing_still(shape, point):
            shape.add(point)
            return 1
        elif _can_fall_down(shape, point):
            point = point[0], point[1] + 1
        elif _can_fall_left(shape, point):
            point = point[0] - 1, point[1] + 1
        elif _can_fall_right(shape, point):
            point = point[0] + 1, point[1] + 1


def _add_solid_floor(shape: set[Point], solid_floor_level: int) -> None:
    max_x = max(x for x, _ in shape)
    min_x = min(x for x, _ in shape)
    infinity_size = 500
    for x in range(min_x - infinity_size, max_x + infinity_size):
        shape.add((x, solid_floor_level))


def count(shape: set[Point]) -> int:
    counter = 0
    platform_level = max(y for x, y in shape)
    while True:
        try:
            counter += _try_to_fall(shape, SOURCE, platform_level)
        except ToTheMoon:
            return counter


def count2(shape: set[Point]) -> int:
    counter = 0
    platform_level = max(y for x, y in shape)
    solid_floor_level = platform_level + 2
    _add_solid_floor(shape, solid_floor_level)
    while SOURCE not in shape:
        counter += _try_to_fall(shape, SOURCE, solid_floor_level)
    return counter


if __name__ == "__main__":
    # print(test_input_data)
    assert count(get_data(TEST_INPUT_FILE)) == 24
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(get_data(TEST_INPUT_FILE)) == 93
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
