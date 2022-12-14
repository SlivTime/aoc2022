import heapq
import string
from typing import Generator

INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"
Coord = tuple[int, int]
Map = list[list[str]]

START_NODE = 'S'
END_NODE = 'E'

INF = float('inf')

HEIGHTS = f'{START_NODE}{string.ascii_lowercase}{END_NODE}'


def _prepare(line: str):
    return [char for char in line.strip()]


def get_data(filename: str) -> Map:
    with open(filename) as f:
        data = [_prepare(line) for line in f]
    return data


def _find_start(data: Map, ) -> Coord:
    return next(_find_start_points(data, {START_NODE}))


def _find_start_points(data: Map, start_points) -> Generator[Coord, None, None]:
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char in start_points:
                yield x, y


def _find_end(data: Map) -> Coord:
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "E":
                return x, y
    raise ValueError("No end found")


def _get_neighbors(position: Coord) -> list[Coord]:
    return [
        (position[0] + 1, position[1] + 0),
        (position[0] + 0, position[1] - 1),
        (position[0] + 0, position[1] + 1),
        (position[0] - 1, position[1] + 0),
    ]


def _get_height(data: Map, position: Coord) -> str | None:
    x, y = position
    if x < 0 or y < 0:
        return None
    try:
        return data[position[0]][position[1]]
    except IndexError:
        return None


def _could_be_next(step: str, next_step: str) -> bool:
    if step == END_NODE:
        return False
    next_idx = HEIGHTS.index(step) + 1
    possible = HEIGHTS[:next_idx + 1]
    return next_step in possible


def _next_steps(data: Map, current: Coord) -> list[Coord]:
    result = []
    x, y = current
    cur_height = _get_height(data, current)
    if _get_height(data, current) == 'j' and x in range(20, 30) and y in range(140, 150):
        ...

    if cur_height == 'z':
        ...
    for n in _get_neighbors(current):
        neighbor_height = _get_height(data, n)
        if neighbor_height is None:
            continue
        if _could_be_next(cur_height, neighbor_height):
            result.append(n)

    return result


def _build_distances(map: Map, start: Coord, end: Coord) -> dict[Coord, int | float]:
    distances = {
        # coord, dist_from_zero
        start: 0,
    }
    seen = set()
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        _, p = heapq.heappop(queue)
        if p in seen:
            continue
        dist_from_start = distances[p]
        neighbors = _next_steps(map, p)
        for n in neighbors:
            n_dist = distances.get(n, INF)
            if dist_from_start + 1 < n_dist:
                distances[n] = dist_from_start + 1
            if n not in seen:
                heapq.heappush(queue, (distances[n], n))
        seen.add(p)
    return distances


def count1(data):
    start = _find_start(data)
    end = _find_end(data)
    distances = _build_distances(data, start, end)
    return distances[end]


def count2(data: list[tuple[str, str]]) -> int:
    variants = []
    end = _find_end(data)
    for start_point in _find_start_points(data, {START_NODE, 'a'}):
        distances = _build_distances(data, start_point, _find_end(data))
        if end in distances:
            variants.append(distances[end])
    return min(variants)


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    assert count1(test_input_data) == 31
    print(f"Part 1: {count1(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 29
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
