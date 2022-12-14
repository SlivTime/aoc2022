import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from types import FunctionType




@dataclass
class Monkey:
    items: list[int]
    operation: FunctionType
    test: int
    true_case: int
    false_case: int


TEST_STATE = [
    Monkey(
        items=[79, 98],
        operation=lambda x: x * 19,
        test=23,
        true_case=2,
        false_case=3,
    ),
    Monkey(
        items=[54, 65, 75, 74],
        operation=lambda x: x + 6,
        test=19,
        true_case=2,
        false_case=0,
    ),
    Monkey(
        items=[79, 60, 97],
        operation=lambda x: x * x,
        test=13,
        true_case=1,
        false_case=3,
    ),
    Monkey(
        items=[74],
        operation=lambda x: x + 3,
        test=17,
        true_case=0,
        false_case=1,
    ),
]

PROD_STATE = [
    Monkey(
        items=[54, 82, 90, 88, 86, 54],
        operation=lambda x: x * 7,
        test=11,
        true_case=2,
        false_case=6,
    ),
    Monkey(
        items=[91, 65],
        operation=lambda x: x * 13,
        test=5,
        true_case=7,
        false_case=4,
    ),
    Monkey(
        items=[62, 54, 57, 92, 83, 63, 63],
        operation=lambda x: x + 1,
        test=7,
        true_case=1,
        false_case=7,
    ),
    Monkey(
        items=[67, 72, 68],
        operation=lambda x: x * x,
        test=2,
        true_case=0,
        false_case=6,
    ),
    Monkey(
        items=[68, 89, 90, 86, 84, 57, 72, 84],
        operation=lambda x: x + 7,
        test=17,
        true_case=3,
        false_case=5,
    ),
    Monkey(
        items=[79, 83, 64, 58],
        operation=lambda x: x + 6,
        test=13,
        true_case=3,
        false_case=0,
    ),
    Monkey(
        items=[96, 72, 89, 70, 88],
        operation=lambda x: x + 4,
        test=3,
        true_case=1,
        false_case=2,
    ),
    Monkey(
        items=[79],
        operation=lambda x: x + 8,
        test=19,
        true_case=4,
        false_case=5,
    ),
]


def _readable_state(state: list[Monkey]) -> None:
    readable = []
    for idx, monkey in enumerate(state):
        readable.append(f'Monkey {idx}: {monkey.items}')
    return '\n'.join(readable)


def _count(state: list[Monkey], rounds: int, bored_func: FunctionType) -> int:
    monkey_actions = defaultdict(int)
    modulo = math.prod(monkey.test for monkey in state)
    for rnd in range(rounds):
        for idx, monkey in enumerate(state):
            for item in monkey.items:
                monkey_actions[idx] += 1
                new_item = monkey.operation(item)
                after_bored = bored_func(new_item)
                after_bored = after_bored  % modulo
                if after_bored % monkey.test == 0:
                    state[monkey.true_case].items.append(after_bored)
                else:
                    state[monkey.false_case].items.append(after_bored)
            monkey.items = []
        # print(rnd, _readable_state(state), '\n')
    # print(state)
    print(monkey_actions)
    sorted_actions = sorted(monkey_actions.values(), reverse=True)
    return sorted_actions[0] * sorted_actions[1]

def count(state: list[Monkey]) -> int:
    return _count(state, 20, lambda x: int(x / 3))

def count2(state: list[Monkey]) -> int:
    return _count(state, 10000, lambda x: x)


if __name__ == "__main__":
    # assert count(TEST_STATE) == 10605
    # print(f"Part 1: {count(PROD_STATE)}")
    assert count2(TEST_STATE) == 2713310158
    print(f"Part 2: {count2(PROD_STATE)}")
