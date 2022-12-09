INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

Coord = tuple[int, int]


def _prepare(line: str):
    return line


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def _build_head_path(commands: list[str]) -> list[Coord]:
    position = (0, 0)
    path = [position]
    for command in commands:
        way, dist = command.split()
        dist = int(dist)
        while dist > 0:
            match way:
                case "U":
                    next = (position[0] + 1, position[1])
                case "D":
                    next = (position[0] - 1, position[1])
                case "R":
                    next = (position[0], position[1] + 1)
                case "L":
                    next = (position[0], position[1] - 1)
            position = next
            path.append(position)
            dist -= 1

    return path


def _get_neighbors(position: Coord) -> list[Coord]:
    return [
        (position[0] + 1, position[1] + 0),
        (position[0] + 1, position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 0, position[1] - 1),
        (position[0] + 0, position[1] + 1),
        (position[0] - 1, position[1] + 0),
        (position[0] - 1, position[1] + 1),
        (position[0] - 1, position[1] - 1),
    ]


def _guess_next_move(tail_pos: Coord, head_pos: Coord) -> Coord:
    neighbor_distances: list[tuple[int, Coord]] = []
    for n_coord in _get_neighbors(tail_pos):
        new_dist = _get_distance(head_pos, n_coord)
        neighbor_distances.append((new_dist, n_coord))
    neighbor_distances.sort(key=lambda x: x[0])
    return neighbor_distances[0][1]


def _build_tail_path(head_path: list[Coord]) -> list[Coord]:
    path = [head_path[0]]
    position = path[0]
    for move in head_path:
        if _get_distance(position, move) >= 2:
            next = _guess_next_move(position, move)
            path.append(next)
            position = next
    return path


def _get_distance(p1: Coord, p2: Coord) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def count(data: list[str]) -> int:
    head_path = _build_head_path(data)
    tail_path = _build_tail_path(head_path)
    res = len(set(tail_path))
    return res


def count2(data: list[str]) -> int:
    rope_len = 10
    paths = []
    knot_path = _build_head_path(data)
    for knot in range(rope_len - 1):
        knot_path = _build_tail_path(knot_path)
        paths.append(knot_path)
    tail_path = paths[-1]
    res = len(set(tail_path))
    return res


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    assert count(test_input_data) == 13
    print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 1
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
