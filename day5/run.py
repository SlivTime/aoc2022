import re
from pprint import pprint
import more_itertools
from collections import defaultdict

INPUT_FILE = "input.txt"
TEST_INPUT_FILE = "test_input.txt"

stack_regex = re.compile('[A-Z]')
action_regex = re.compile('\d+')


def _parse_action(line: str) -> tuple[int, str, str]:
    print(line)
    count, source, target = action_regex.findall(line)
    return [int(x) for x in (count, source, target)]

def get_data(filename: str) -> tuple[dict[int, list[str], list[str]]]:
    stacks = defaultdict(list)
    actions = []
    with open(filename) as f:
        # parse stacks
        for line in f:
            if line == '\n':
                break
            for idx, chunk in enumerate(more_itertools.sliced(line, 4), start=1):
                found = stack_regex.findall(chunk)
                if found:
                    stacks[idx].insert(0, found[0])

        # parse actions:
        for line in f:
            actions.append(
                _parse_action(line)
            )

    return stacks, actions



def count(data: tuple[dict[str, list[str], list[str]]]) -> str:
    stacks, actions = data
    for action in actions:
        count, source, target = action
        for _ in range(count):
            item = stacks[source].pop()
            stacks[target].append(item)
            print(stacks)

    ordered_keys = sorted(stacks)
    res = ""
    for key in sorted(stacks):
        if stacks[key]:
            res += more_itertools.last(stacks[key])        
    
    return res



def count2(data: tuple[dict[str, list[str], list[str]]]) -> str:
    stacks, actions = data
    for action in actions:
        count, source, target = action
        pack = stacks[source][-count:]
        stacks[source] = stacks[source][:-count]
        stacks[target] += pack

    ordered_keys = sorted(stacks)
    res = ""
    for key in sorted(stacks):
        if stacks[key]:
            res += more_itertools.last(stacks[key])        
    
    return res


if __name__ == "__main__":
    test_input_data = get_data(TEST_INPUT_FILE)
    print(test_input_data)
    # assert count(test_input_data) == 'CMZ'
    # print(f"Part 1: {count(get_data(INPUT_FILE))}")
    assert count2(test_input_data) == 'MCD'
    print(f"Part 2: {count2(get_data(INPUT_FILE))}")
