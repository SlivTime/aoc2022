INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

COORD = tuple[int, int]


def _prepare(line: str) -> list[int]:
    return [int(x) for x in line.strip()]


def get_data(filename: str) -> list[list[int]]:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def _get_tree(coords: COORD, forest: list[list[int]]) -> int | None:
    x, y = coords
    if x < 0 or y < 0:
        return None
    try:
        return forest[x][y]
    except IndexError:
        return None


def _get_directions_heights(coords: COORD, forest: list[list[int]]) -> list[int]:
    x, y = coords
    max_x = len(forest)
    max_y = len(forest[0])
    if x in (0, max_x - 1) or y in (0, max_y - 1):
        return [-1]
    up = [(i, y) for i in range(x)]
    left = [(x, i) for i in range(y)]
    right = [(x, i) for i in range(y + 1, max_y)]
    down = [(i, y) for i in range(x + 1, max_x)]
    up_h = max([_get_tree(coords, forest) for coords in up])
    up_l = max([_get_tree(coords, forest) for coords in left])
    up_r = max([_get_tree(coords, forest) for coords in right])
    up_d = max([_get_tree(coords, forest) for coords in down])
    return [up_d, up_h, up_l, up_r]


def _look_at_direction(
    coords: COORD, forest: list[list[int]], direction: list[COORD]
) -> list[int]:
    visible = 0
    this_tree = _get_tree(coords, forest)
    for n_coords in direction:
        next_tree = _get_tree(n_coords, forest)
        if next_tree is None:
            break
        visible += 1
        if next_tree >= this_tree:
            break
    return visible


def _get_visible_from_here(coords: COORD, forest: list[list[int]]) -> list[int]:
    x, y = coords
    max_x = len(forest)
    max_y = len(forest[0])

    up = list(reversed([(i, y) for i in range(x)]))
    down = [(i, y) for i in range(x + 1, max_x)]
    left = list(reversed([(x, i) for i in range(y)]))
    right = [(x, i) for i in range(y + 1, max_y)]

    visible = []
    for direction in (up, right, down, left):
        visible.append(_look_at_direction(coords, forest, direction))

    return visible


def count(forest: list[list[int]]) -> int:
    visible = set()
    for x, row in enumerate(forest):
        for y, height in enumerate(row):
            coord = (x, y)
            heights = _get_directions_heights(coord, forest)
            if height > min(heights):
                visible.add(coord)

    return len(visible)


def _scenic_score(trees_count: list[int]) -> int:
    result = 1
    for trees in trees_count:
        result *= trees
    return result


def count2(forest: list[list[int]]) -> int:
    max_score = 0
    for x, row in enumerate(forest):
        for y, _ in enumerate(row):
            coord = (x, y)
            visible = _get_visible_from_here(coord, forest)
            score = _scenic_score(visible)
            max_score = max(max_score, score)
    return max_score


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    assert count(test_input_data) == 21
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 8
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
